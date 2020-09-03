HOST = ''
PORT = 21566
BUF_SIZE = 1024
ADDR = (HOST, PORT)

class MSG_TYPE:
    MAKE_TORRENT = "make_torrent"
    DOWNLOAD = "download"
    SEEDING = "seeding"