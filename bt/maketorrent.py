import sys
import os
import libtorrent
import time

dir_path = '/opt/work/code/Python/bt/seed'
fs = libtorrent.file_storage()
libtorrent.add_files(fs, dir_path)
torrent = libtorrent.create_torrent(fs, 0, 4 * 1024 * 1024)
torrent.add_tracker("http://192.168.65.128:6969/announce")
torrent.set_creator('libtorrent %s' % libtorrent.version)
parent_dir = os.path.dirname(dir_path)
libtorrent.set_piece_hashes(torrent, parent_dir, lambda x: sys.stderr.write(str(x)))
raw = torrent.generate()
print
''
print
libtorrent.make_magnet_uri(libtorrent.torrent_info(raw))
with open("/opt/work/code/Python/bt/1.torrent", "wb") as f:
    f.write(libtorrent.bencode(raw))