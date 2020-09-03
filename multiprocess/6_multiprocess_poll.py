#!/usr/bin/python2.7

from multiprocessing import Pool
import time
import os
import sys
def action(name='http://c.biancheng.net'):
    print(name,' --current pid', os.getpid())
    if name == "nihao":
        time.sleep(5)
        print ("return ")
        return 1
    else:
        time.sleep(10)
        print ("return ")
        return 2

def exit_proc(arg):
    print (arg)
    #sys.exit() # process no exit
    #os._exit() # process directly exit


# method 2 metaclass
# class Singleton(type):
#     def __init__(self, name, bases, class_dict):
#         print ('Singleton init')
#         super(Singleton, self).__init__(name, bases, class_dict)
#         self._instance = None
#     def __call__(self, *args, **kwargs):
#         print ('Singleton call')
#         if self._instance is None:
#             self._instance = super(Singleton, self).__call__(*args, **kwargs)
#         return self._instance
    

class MakeTorrent():
    # __metaclass__ = Singleton #py2 ok, py3 no
    def __init__(self, process_num=1):
        print("init create process pool")
        self.pool = Pool(processes=4)
        # self.pool = pool
    
    def run(self):
        print("run make task a")
        # self.pool.apply_async(self._proc_make_torrent, kwds={"type":"make", "info":"you want info"})

        def _make_torrent():
            print(' --current pid', os.getpid())
            print('_make_torrent')

        self.pool.apply_async(_make_torrent)

    def __call__(self, *args, **kwargs):
        print("you call me")

    def _proc_make_torrent(self, info=""):
        print(' --current pid', os.getpid())
        # print(type)
        print(info)
        time.sleep(5)
    
if __name__ == '__main__':
    debug = 1

    # obj = MakeTorrent()
    # obj.run()
    # time.sleep (10)

    if debug == 1:
        pool = Pool(processes=4)
        pool.apply_async(action)
        pool.apply_async(action, args=('nihao', ), callback=exit_proc)
        pool.apply_async(action, args=('hello', ))
        pool.apply_async(action, args=('nishsuosha', ))
        # pool.apply_async(action, args=('xx1', ))
        # pool.apply_async(action, args=('xx2', ))
        # pool.apply_async(action, args=('xx3', ))
        pool.close()
        pool.join()
