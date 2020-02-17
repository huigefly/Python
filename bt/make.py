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
g_handle = None

def func(piece_index):
    sys.stderr.write('.')

def make_torrent(file, tracker, save_dir):
    print("file:%s" % file)
    print("tracker:%s" % tracker)
    print("save:%s" % save_dir)
    print('version:%s' % lt.version)

    fs = lt.file_storage()      # get file storage obj
    lt.add_files(fs, file)      # add files to file storage
    print("fs files:%d" % fs.num_files())
    if fs.num_files() == 0:     # check 
        os._exit(0)
    t = lt.create_torrent(fs, PIECE_SIZE, PAD_FILE_SIZE)   
    print("picesize:%s" % t.piece_size(0))
    t.add_tracker(tracker)
    t.set_creator('libtorrent %s' % lt.version)  # optional. 

    # real start create torrent
    lt.set_piece_hashes(t, os.path.dirname(file), func) # base file in this directory, fun callback

    # write to torrent file
    basename = os.path.basename(file)
    torrent_name = os.path.join(save_dir, basename + ".torrent")
    print("torrent:%s" % torrent_name)
    f = open(torrent_name, "wb+")
    f.write(lt.bencode(t.generate()))  #generere: create bencode file. 
    f.close()


def handle_alert(alert):
    alert_type = alert.what()
    if alert_type == "torrent_finished_alert":
        print("msg:", alert.message())
        # handle = alert.handle
        # create fast resume
        # if handle.is_valid() and handle.has_metadata():
        #     data = lt.bencode(handle.write_resume_data())
        #     temp = "/opt/work/code/Python/bt/temp/" + alert.handle.name() + '.fastresume'
        #     open(temp, 'wb').write(data)
        return 1
    elif alert_type == "state_update_alert":
        # alert.handle.save_resume_data()
        t_state = ['queued', 'checking', 'downloading metadata', \
            'downloading', 'finished', 'seeding', \
            'allocating', 'checking fastresume']
        if len(alert.status) > 0:
            s = alert.status[0]
            print("state:%s" % t_state[s.state])
            print("download load:%dkb/s" % (s.download_payload_rate / 1000))
            print("progress:%f" % (s.progress_ppm / 10000))
    elif alert_type == "save_resume_data_alert":
        # print("msg:", alert.message())
        # print("save_resume_data_alert:", alert.handle.name())
        temp = "/opt/work/code/Python/bt/temp/" + alert.handle.name() + '.fastresume'
        with open(temp, 'wb+') as f:
            data = lt.bencode(alert.handle.write_resume_data())
            f.write(data)
    elif alert_type == "save_resume_data_failed_alert":
        print("msg:", alert.message())
    # else:
    #     print("alert_type:", alert_type)


def share_torrent(torrent, save_dir, name):
    settings = lt.session_settings()
    settings.user_agent = 'python_client/' + lt.version
    settings.ignore_limits_on_local_network = False
    settings.disable_hash_checks = True
    
    ses.set_settings(settings)
    ses.set_alert_mask(0xfffffff)
    # ses.set_alert_mask(lt.alert.category_t.status_notification | lt.alert.category_t.storage_notification)
    
    atp = {}
    atp["save_path"] = save_dir
    atp["storage_mode"] = lt.storage_mode_t.storage_mode_sparse
    # atp["storage_mode"] = lt.storage_mode_t.storage_mode_compact
    # atp["storage_mode"] = lt.storage_mode_t.storage_mode_allocate
    atp["paused"] = False
    atp["auto_managed"] = True
    atp["duplicate_is_error"] = True
    # atp["flags"] = lt.add_torrent_params_flags_t.flag_seed_mode
    atp["name"] = "helloworld_%d" % threading.currentThread().ident
    temp = "/opt/work/code/Python/bt/temp/" + name + '.fastresume'
    if os.path.exists(temp):
        print("read torrent", temp)
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
    handle.set_upload_limit(200000)
    g_handle_queue.put(handle)

    alive = True
    while alive:
        alerts = []
        while 1:
            a = ses.pop_alert()
            if not a: 
                break
            alerts.append(a)

        # print("alert:", len(alerts))
        for a in alerts:
            rtn = handle_alert(a)
            if rtn == 1:
                alive = False
                break
        ses.post_torrent_updates()
        if handle and handle.need_save_resume_data():
            print("-- handle save resume data")
            handle.save_resume_data()
        time.sleep(0.2)
    

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
        info["torrent"] = "/opt/work/code/Python/bt/seed/3.mp4.torrent"
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
        # t2 = threading.Thread(target=download_proc, args=(params2, ))

        t1.start()
        # t2.start()

        t1.join()
        # t2.join()

        print("handle queue:", g_handle_queue.qsize())

        # time.sleep(100000)
    
