from msg_handle_base import MsgHandleBase

class MakeTorrentInfo:
    def __init__(self):
        self.source_file = ""
        self.save_path = ""
        self.tracker_url = ""

class MsgHandleMakeTorrent(MsgHandleBase):
    def run(self):
        print("make torrent:%s" % self.data)
        pass