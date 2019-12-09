#!/usr/bin/python2.7

import time
import os
import sys
from multiprocessing import Process

class Run(Process):
    def __init__(self, name, second, deamon = False):
        # super().__init__()   # python3.5 is ok
        Process.__init__(self)
        Process.daemon = deamon    # deamon: need process always in backgroud, is true. when main process exit, it exit
        self.__name = name
        self.__second = second

    def run(self):
        print('pid:%d, name:%s runing' % (os.getpid(), self.__name))
        time.sleep(self.__second)
        print('pid:%d, name:%s runing end' % (os.getpid(), self.__name))


def test():
    print("--enter test, pid:%d" % os.getpid())

    p1 = Run('anne', 2, True)
    p2 = Run('alex', 5)

    p1.start() 
    p2.start()

    print('--exit main process')
    sys.exit(0)   # exit, but not exit process. os._exit: directly exit


if "__main__" == __name__:
    test()
