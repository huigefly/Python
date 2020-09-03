from msg_handle_base import MsgHandleBase
import multiprocessing
import time
import os

def proc_make_torrent(data):
    print("pid:%s, recv data:%s" % (os.getpid(), data))
    time.sleep(5)
    print("recv end")

class MakeTorrentInfo:
    def __init__(self, source_file="", save_path = "", tracker_url = "", source_file_change_time = ""):
        self.source_file = ""
        self.save_path = ""
        self.tracker_url = ""
        self.source_file_change_time = ""


class MsgHandleMakeTorrent(MsgHandleBase):
    def __init__(self):
        # print("init MsgHandleMakeTorrent:%s" % self.list_task.size())
        if self._instance is None:
            print("init MsgHandleMakeTorrent none")
        else:
            print("init MsgHandleMakeTorrent")
        self.list_task = {}

    def run(self):
        print("start process make torrent")
        self._parse_data(self.data)
        p = multiprocessing.Process(target=proc_make_torrent, args=(self.data,))
        p.start()

    def _parse_data(self, data):
        info = data.split('#')
        source_file = info[1]
        save_path = info[2]
        tracker_url = info[3]
        change_time = os.path.getmtime(source_file)

        makeTorrentInfo = MakeTorrentInfo(source_file, save_path, tracker_url, change_time)
        if source_file not in self.list_task or self.list_task[source_file].source_file_change_time != change_time:
            self.list_task[source_file] = makeTorrentInfo


        
