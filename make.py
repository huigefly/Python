#!/usr/bin/python2.7
import libtorrent as lt
import sys
import os

PIECE_SIZE = 0  # auto calc file ,get size . if 0, automatic; min 16k max 2m. file.size / 20k
PAD_FILE_SIZE = 4 * 1024 * 1024 # flag is optimize_alignment, is valid. disk io good
g_total_pieces = 0

def func(piece_index):
    sys.stderr.write('.' + str(piece_index))

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
    g_total_pieces = t.num_pieces()     # get total piece nums
    print("piece total:%d" % g_total_pieces)
    print("picesize:%s" % t.piece_size(0))

    t.add_tracker(tracker)
    t.set_creator('libtorrent %s' % lt.version)  # optional. 

    # real start create torrent
    lt.set_piece_hashes(t, os.path.dirname(file), func) # base file in this directory, fun callback

    # write to torrent file
    basename = os.path.basename(file)
    torrent_name = os.path.join(save_dir, basename + ".torrent")
    print("\ntorrent:%s" % torrent_name)

    #generere: create bencode file. 
    with open(torrent_name, "wb+") as f:
        f.write(lt.bencode(t.generate()))

if "__main__" == __name__:
    print("usage:   file tracker save_dir\n")
    make_torrent(sys.argv[1],sys.argv[2],sys.argv[3])

