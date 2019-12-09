import libtorrent as lt
import sys

def showinfo(torrent_abspath):
    try:
        fd = open(torrent_abspath, 'rb')
        torrent_data = lt.bdecode(fd.read())
        print (torrent_data)
        torrent = lt.torrent_info(torrent_data)
        fd.close()
        return torrent
    except Exception as ex:
        print("torrent info error: %s\nstatck msg:%s" % (torrent_abspath, ex))
       
if "__main__" == __name__:
    value = showinfo(sys.argv[1])
    print (value)