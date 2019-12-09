#!/usr/bin/python2.7

import time
import random
import os
from multiprocessing import Process


def run(name):
    print('%s runing, pid:%d' % (name, os.getpid()))
    time.sleep(random.randrange(1,5))
    print('%s running end' %name)

def test():
    print("--enter test, pid:%d" % os.getpid())

    p1=Process(target=run, args=('anne',))
    p2=Process(target=run, args=('alice',))
    p3=Process(target=run, args=('biantai',))
    p4=Process(target=run, args=('haha',))

    p1.start()
    p2.start()
    p3.start()
    p4.start()
    print('--exit main process')

if "__main__" == __name__:
    test()