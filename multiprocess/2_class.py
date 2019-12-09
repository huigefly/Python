#!/usr/bin/python2.7

import time
import random
import os
import sys
from multiprocessing import Process

class Run(Process):
    def __init__(self,name):
        # super().__init__()   # python3.5 is ok
        Process.__init__(self)
        self.name=name

    def run(self):
        print('pid:%d, name:%s runing' % (os.getpid(), self.name))
        time.sleep(random.randrange(1,5))
        print('pid:%d, name:%s runing end' % (os.getpid(), self.name))


def test():
    print("--enter test, pid:%d" % os.getpid())

    p1 = Run('anne')
    p2 = Run('alex')
    p3 = Run('ab')
    p4 = Run('hey')

    p1.start() 
    p2.start()
    p3.start()
    p4.start()

    p1.join() 
    p2.join()
    p3.join()
    p4.join()

    print('--exit main process')
    sys.exit(0)   # exit, but not exit process. os._exit: directly exit


if "__main__" == __name__:
    test()
