import sys
import time
import os
import libtorrent as lt

PIECE_SIZE = 0 # auto calc file ,get size . if 0, automatic; min 16k max 2m. file.size / 20k
PAD_FILE_SIZE = 4 * 1024 * 1024 # flag is optimize_alignment, is valid. disk io good

def func(piece_index):
    # print("0:", piece_index)
    a = 1

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


def share_torrent(torrent, save_dir):
    settings = lt.session_settings()
    settings.user_agent = 'python_client/' + lt.version
    settings.ignore_limits_on_local_network = False

    ses = lt.session()
    ses.listen_on(6888, 6888 + 300)
    ses.set_settings(settings)
    ses.set_alert_mask(lt.alert.category_t.tracker_notification)

    atp = {}
    atp["save_path"] = save_dir
    atp["storage_mode"] = lt.storage_mode_t.storage_mode_sparse
    atp["paused"] = False
    atp["auto_managed"] = True
    atp["duplicate_is_error"] = True
    info = None
    try:
        fd = open(torrent, 'rb')
        torrent_data = lt.bdecode(fd.read())
        info = lt.torrent_info(torrent_data)
        fd.close()
    except Exception as ex:
        print("torrent info error: %s\nstatck msg:%s" % (torrent, ex))

    basename = info.name()
    print('download add: \'%s\'...' % basename)
    atp["ti"] = info
    handle = ses.add_torrent(atp)
    handle.set_max_connections(60)
    handle.set_max_uploads(-1)
    handle.set_download_limit(-1)
    handle.set_upload_limit(-1)

    while True:
        s = handle.status()
        print (s.state)
        if s.state == lt.torrent_status.seeding or s.state == lt.torrent_status.finished:
            print("torrent seeding")
            break
        time.sleep(1)
    # keep handle, share torrent
    time.sleep(100000)

if "__main__" == __name__:
    print("usage:\n" +
            "\tmake file tracker save\n" + 
            "\tshare torrent save\n")
    if sys.argv[1] == "make":
        make_torrent(sys.argv[2], sys.argv[3], sys.argv[4])
    elif sys.argv[1] == "share": 
        share_torrent(sys.argv[2], sys.argv[3])

    