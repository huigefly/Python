#!/usr/bin/python2.7

from priority_deque import PriorityQueue
from Queue import Queue
from threading import Thread, Event
import time

# A thread that produces data
def producer(out_q):
    running = True
    count = 1
    data = "helloworld"
    while running:
        if count > 10: 
            break
        
        evt = Event()
        data = "helloworld_%d" % count
        print("produce:%s" % data)
        # Produce some data
        out_q.put((data, evt), count)
        # out_q.put(data)
        count += 1

        evt.wait()  # wait consumer consume
        # time.sleep(2)

# A thread that consumes data
def consumer(in_q):
    time.sleep(2)
    while True:
        # Get some data
        data, evt = in_q.get(timeout=5)
        
        # Process the data
        print ("consumer:%s" % data)

        evt.set()
        # Indicate completion
        # in_q.task_done()

# Create the shared queue and launch both threads
q = PriorityQueue()
# q = Queue()

t1 = Thread(target=consumer, args=(q,))
t2 = Thread(target=producer, args=(q,))

t1.start()
t2.start()

# Wait for all produced items to be consumed
# q.join()