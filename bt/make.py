import sys
import time
import os
import libtorrent as lt

def make_torrent(file, tracker, save_dir):
    fs = lt.file_storage()
    lt.add_files(fs, file)
    print("fs files:%d" % fs.num_files())
    if fs.num_files() == 0:
        os._exit(0)
    t = lt.create_torrent(fs, 0, 4 * 1024 * 1024)
    t.add_tracker(tracker)
    t.set_creator('libtorrent %s' % lt.version)
    lt.set_piece_hashes(t, save_dir, lambda x: sys.stderr.write('.'))
    sys.stderr.write('\n')

    f = open(file + ".torrent", "wb+")
    # print >> f, libtorrent.bencode(t.generate())
    f.write(lt.bencode(t.generate()))
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
        if s.state == lt.torrent_status.seeding or s.state == lt.torrent_status.finished:
            print("torrent seeding")
            break
        time.sleep(1)
    # keep handle, share torrent
    time.sleep(100000)

if "__main__" == __name__:
    make_torrent(sys.argv[1], sys.argv[2], sys.argv[3])
    share_torrent(sys.argv[1] + ".torrent", sys.argv[3])

    