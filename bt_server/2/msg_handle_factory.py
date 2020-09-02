from constant import MSG_TYPE
from msg_handle.msg_handle_make_torrent import MsgHandleMakeTorrent
from msg_handle.msg_handle_download import MsgHandleDownload
from msg_handle.msg_handle_seeding import MsgHandleSeeding

class MsgHandleFactory():
    @classmethod
    def get(cls, msg_type):
        if msg_type == MSG_TYPE.MAKE_TORRENT:
            return MsgHandleMakeTorrent()
        elif msg_type == MSG_TYPE.DOWNLOAD:
            return MsgHandleDownload()
        elif msg_type == MSG_TYPE.SEEDING:
            return MsgHandleSeeding()

        

