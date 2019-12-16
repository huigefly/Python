#!/usr/bin/python2.7

import sys
import time
import os
import libtorrent as lt
import threading
from Queue import Queue

PIECE_SIZE = 0 # auto calc file ,get size . if 0, automatic; min 16k max 2m. file.size / 20k
PAD_FILE_SIZE = 4 * 1024 * 1024 # flag is optimize_alignment, is valid. disk io good

g_handle_queue = Queue()
ses = lt.session()
ses.listen_on(6888, 6888 + 300)
ses.set_alert_mask(lt.alert.category_t.tracker_notification)

def func(piece_index):
    sys.stderr.write('.')

def make_torrent(file, tracker, save_dir):
    print("file:%s" % file)
    print("tracker:%s" % tracker)
    print("save:%s" % save_dir)
    print('version:%s' % lt.version)

    fs = lt.file_storage()
    lt.add_files(fs, file)
    print("fs files:%d" % fs.num_files())
    if fs.num_files() == 0:
        os._exit(0)
    t = lt.create_torrent(fs, PIECE_SIZE, PAD_FILE_SIZE)
    print("picesize:%s" % t.piece_size(0))
    t.add_tracker(tracker)
    t.set_creator('libtorrent %s' % lt.version)
    lt.set_piece_hashes(t, os.path.dirname(file), func) # base file in this directory, fun callback

    basename = os.path.basename(file)
    torrent_name = os.path.join(save_dir, basename + ".torrent")
    print("torrent:%s" % torrent_name)
    f = open(torrent_name, "wb+")
    f.write(lt.bencode(t.generate()))  #generere: create bencode file. 
    f.close()


def share_torrent(torrent, save_dir, name):
    t_state = ['queued', 'checking', 'downloading metadata', \
            'downloading', 'finished', 'seeding', \
            'allocating', 'checking fastresume']

    settings = lt.session_settings()
    settings.user_agent = 'python_client/' + lt.version
    settings.ignore_limits_on_local_network = False
    settings.disable_hash_checks = True
    
    ses.set_settings(settings)
    # ses.set_alert_mask(0xfffffff)
    ses.set_alert_mask(lt.alert.category_t.status_notification)
    
    atp = {}
    atp["save_path"] = save_dir
    # atp["storage_mode"] = lt.storage_mode_t.storage_mode_sparse
    atp["storage_mode"] = lt.storage_mode_t.storage_mode_compact
    # atp["storage_mode"] = lt.storage_mode_t.storage_mode_allocate
    atp["paused"] = False
    atp["auto_managed"] = True
    atp["duplicate_is_error"] = True
    # atp["flags"] = lt.add_torrent_params_flags_t.flag_seed_mode
    atp["name"] = "helloworld_%d" % threading.currentThread().ident
    temp = "/opt/work/code/Python/bt/" + name + '.fastresume'
    if os.path.exists(temp):
        atp["resume_data"] = open(temp, 'rb').read()
    info = None
    try:
        fd = open(torrent, 'rb')
        torrent_data = lt.bdecode(fd.read())
        info = lt.torrent_info(torrent_data)
        fd.close()
    except Exception as ex:
        print("torrent info error: %s\nstatck msg:%s" % (torrent, ex))

    basename = info.name()
    print("download add: %s..." % basename)
    atp["ti"] = info
    handle = ses.add_torrent(atp)
    handle.set_max_connections(60)
    handle.set_max_uploads(-1)
    handle.set_download_limit(-1)
    handle.set_upload_limit(-1)
    g_handle_queue.put(handle)

    alive = True
    while alive:
        ### old way
        # s = handle.status()
        # print ("tid:", threading.currentThread().ident, t_state[s.state], handle.name())
        # if s.state == lt.torrent_status.seeding or s.state == lt.torrent_status.finished:
        #     print("torrent seeding")
        #     handle.save_resume_data()
        #     break
        # handle.save_resume_data()
        
        alerts = []
        while 1:
            a = ses.pop_alert()
            if not a: break
            alerts.append(a)

        print("alert:", len(alerts))
        for a in alerts:
            # if a.category() == lt.alert.category_t.status_notification:
            #     print(a.message() + '\n')
            if a.what() == "torrent_finished_alert":
                print("msg:", a.message())
                alive = False
                break

            # if a.what() == lt.torrent_added_alert.what():
            #     print(a.message() + '\n')
            # if type(a) == str:
            #     print(a + '\n')
            # else:
            #     print(a.message() + '\n')

        time.sleep(1)

    # create fast resume
    # if handle.is_valid() and handle.has_metadata():
    #         data = lt.bencode(handle.write_resume_data())
    #         open(os.path.join(save_dir, handle.get_torrent_info().name() + '.fastresume'), 'wb').write(data)

def download_proc(p):
    
    for info in p:
        print("tid:", threading.currentThread().ident, info["torrent"], info["save"])
        share_torrent(info["torrent"], info['save'], info["name"])

if "__main__" == __name__:
    print("usage:\n" +
            "\tmake file tracker save\n" + 
            "\tshare torrent save\n")
    if sys.argv[1] == "make":
        make_torrent(sys.argv[2], sys.argv[3], sys.argv[4])
    elif sys.argv[1] == "share": 
        # share_torrent(sys.argv[2], sys.argv[3])
        params1 = []
        info = {}
        info["torrent"] = "/opt/work/code/Python/bt/seed/1.mp4.torrent"
        info["save"] = sys.argv[2]
        info["name"] = "1.mp4"
        params1.append(info)
        
        params2 = []
        info = {}
        info["torrent"] = "/opt/work/code/Python/bt/seed/2.mp4.torrent"
        info["save"] = sys.argv[2]
        info["name"] = "2.mp4"
        params2.append(info)


        t1 = threading.Thread(target=download_proc, args=(params1, ))
        t2 = threading.Thread(target=download_proc, args=(params2, ))

        t1.start()
        t2.start()

        t1.join()
        t2.join()

        print("handle queue:", g_handle_queue.qsize())


    
