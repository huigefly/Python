from rlock import SharedCounter
import threading
import time
from get_more_lock import acquire

a = SharedCounter()
b = SharedCounter()
c = SharedCounter()
d = SharedCounter()
f = SharedCounter()
g = SharedCounter()

x_lock = threading.Lock()
y_lock = threading.Lock()

def proc(v, s):
    while True:
        # with acquire(x_lock):
        #     with acquire(y_lock):
        with acquire(x_lock, y_lock):
            v.incr()
            time.sleep (s)

def mainp(v, s):
    while True:
        # with acquire(y_lock):
        #     with acquire(x_lock):
        with acquire(y_lock, x_lock):   # what gui logic
            time.sleep(1)
            print(s, v._value)

t1 = threading.Thread(target=proc, args=(a,1))
t1.start()

t2 = threading.Thread(target=proc, args=(b,2))
t2.start()

m1 = threading.Thread(target=mainp, args=(a, 'a'))
m1.start()

m2 = threading.Thread(target=mainp, args=(b, 'b'))
m2.start()

m3 = threading.Thread(target=mainp, args=(c, 'c'))
m3.start()
