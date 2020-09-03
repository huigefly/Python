#!/usr/bin/python2.7

import multiprocessing
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

# method 2 metaclass
class Singleton(type):
    def __init__(self, name, bases, class_dict):
        print ('Singleton init')
        super(Singleton, self).__init__(name, bases, class_dict)
        self._instance = None
    def __call__(self, *args, **kwargs):
        print ('Singleton call')
        if self._instance is None:
            self._instance = super(Singleton, self).__call__(*args, **kwargs)
        return self._instance
    
def make_torrent(mylist):
    print("globa make torrent")
    print(mylist) 

class MakeTorrent():
    # __metaclass__ = Singleton #py2 ok, py3 no
    def __init__(self, process_num=1):
        print("init create process pool")
        # global mylist
        with multiprocessing.Manager() as MG:
            self.mylist=MG.list(range(5))
            self.mylist.append("nihao")
    
    def run(self):
        print("run make task a")
        p=multiprocessing.Process(target=make_torrent, 
                                    args=(self.mylist))  
        p.start()

        print(mylist)  

    
if __name__ == '__main__':
    debug = 1

    obj = MakeTorrent()
    obj.run()
    time.sleep (10)

