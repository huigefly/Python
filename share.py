#!/usr/bin/python2.7
import libtorrent as lt
import time
import sys
import os

def share_bt(torrent, save_dir, mode = "download"):
    # define state array
    __state_str = ['queued', 'checking', 'downloading metadata', \
                    'downloading', 'finished', 'seeding', \
                    'allocating', 'checking fastresume']

    # create session
    ses = lt.session()
    ses.listen_on(6888, 6888 + 300)     # set port range. if session use this port, try others. detail see libtorrent:session.hpp
    ses.set_alert_mask(0xfffffff)       # set alert mask, to get you want recv alert type. reference libtorrent:alert.hpp + alert_types.hpp
    # ses.set_alert_mask(lt.alert.category_t.status_notification | lt.alert.category_t.storage_notification)
    
    # create session setting param
    settings = lt.session_settings()    # get session_setting obj
    settings.user_agent = 'python_client/' + lt.version  # set client identification. detail see libtorrent:session_settings.hpp
    settings.ignore_limits_on_local_network = False  # if true, ignore download, updaloc, unchoke limits. 
    ses.set_settings(settings)      # set session_setting to session
    
    # atp: add_torrent_param
    atp = {}
    atp["save_path"] = save_dir             # set save path
    atp["storage_mode"] = lt.storage_mode_t.storage_mode_sparse # have three mode. storage_mode_allocate\storage_mode_compact. detail see libtorrent:storage_defs.hpp
    atp["paused"] = False               # when start download, is start. if ture, auto_managed not True.  detail see libtorrent:add_torrent_params.hpp
    atp["auto_managed"] = True          # if ture , auto resume. detail see libtorrent:add_torrent_params.hpp
    if mode == "seeding":
        atp["flags"] = lt.add_torrent_params_flags_t.flag_seed_mode     # if it is seed, use seed_mode, skip checking. detail see libtorrent:add_torrent_params.hpp
    
    # read torrent, get torrent info
    info = None
    with open(torrent, 'rb') as f:
        torrent_data = lt.bdecode(f.read())
        info = lt.torrent_info(torrent_data)
    basename = info.name()
    print("download add: %s..." % basename)
    atp["ti"] = info

    # try use fast resume
    fast_resume_path = os.path.join(save_dir, info.name() + ".fastresume") 
    print("fast resume name:", fast_resume_path)
    if os.path.exists(fast_resume_path):
        atp["resume_data"] = open(fast_resume_path, 'rb').read()

    # set atp to session, get handle
    handle = ses.add_torrent(atp)

    # set handle param. it also can set in add_torrent_param init. 
    handle.set_max_connections(60)
    handle.set_max_uploads(-1)
    handle.set_download_limit(-1)
    handle.set_upload_limit(-1)

    # run: check status
    while True:
        s = handle.status()
        print(__get_download_status(s, __state_str[s.state]))
        if s.state == lt.torrent_status.seeding or s.state == lt.torrent_status.finished:
            break
        # save resume during downloading and close is good idea.  deaitl see libtorrent:torrent_handle.hpp
        if (int(s.progress * 100) % 2.0) == 0.0:
            if handle.is_valid() and handle.has_metadata():
                data = lt.bencode(handle.write_resume_data())
                with open(os.path.join(save_dir, info.name() + ".fastresume") , 'wb+') as f:
                    f.write(data)
        time.sleep(0.2)

    if handle.is_valid() and handle.has_metadata():
        data = lt.bencode(handle.write_resume_data())
        with open(os.path.join(save_dir, info.name() + ".fastresume") , 'wb+') as f:
            f.write(data)
#    if mode == "seeding":
    time.sleep(1000000)

    # download ok, exit
    ses.pause()

def __get_download_status(s, download_status_flag):
    download_status = {}
    download_status["status"] = download_status_flag
    download_status["progress"] = "%.2f" % (s.progress * 100)
    download_status["download_speed"] = __add_suffix(s.download_rate)
    download_status["upload_speed"] = __add_suffix(s.upload_rate)
    download_status["download_size"] = __add_suffix(s.total_done)
    return download_status

def __add_suffix(val):
    prefix = ['B', 'kB', 'MB', 'GB', 'TB']
    for i in range(len(prefix)):
        if abs(val) < 1000:
            if i == 0:
                return '%.3g%s' % (val, prefix[i])
            else:
                return '%.3g%s' % (val, prefix[i])
        val /= 1000.0
    return '%6.3gPB' % val

if "__main__" == __name__:
    print("usage     torrent save_dir mode[seeding | download]")
    share_bt(sys.argv[1], sys.argv[2], sys.argv[3])
