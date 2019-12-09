#!/usr/bin/python2.7

import os
import io
import time
from concurrent import futures

def handle(name):
    count  = 0
    while True:
        if count > 10:
            break
        print ("pdi:%d, handle:%s" % (os.getpid(), name))
        time.sleep(1)
        count += 1

# according to your param, wait process exit, next
def call():
    with futures.ProcessPoolExecutor(200) as pool:
        results = pool.map(handle, ['hello', 'world', 'what'])
        print ("en:", results)

def return_cb(r):
    print("i konw u:%d, exit" % os.getpid())
    print(r)

def call2():
    with futures.ProcessPoolExecutor(300) as pool:
        for i in ['hello', 'world', 'what']:
            r = pool.submit(handle, i)
            r.add_done_callback(return_cb)
if __name__ == '__main__':
    call2()