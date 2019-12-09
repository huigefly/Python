#!/usr/bin/python2.7
import threading

def worker(n, sema):
    # Wait to be signaled
    sema.acquire()
    # Do some work
    print('Working', n)

# Create some threads
sema = threading.Semaphore(0)
nworkers = 10

for n in range(nworkers):
    t = threading.Thread(target=worker, args=(n, sema,))
    t.start()

sema.release()
sema.release()
sema.release()