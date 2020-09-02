#!/usr/bin/python2.7

from threading import Thread
import time
from collections import deque

# class no herit thread
class CountdownTask:
    def __init__(self):
        self._running = True
        self.history_list_length = 5 
        self.history_list = deque(maxlen=5)

    def terminate(self):
        self._running = False

    def run(self, n):
        while self._running and n > 0:
            print('T-minus', n)
            n -= 1
            self.history_list.append(0.00)
            if len(self.history_list) >= 5:
                history_length = list(set(self.history_list))
                if len(history_length) == 1:
                    print("it is true 1")
            
            print("it is false")
            time.sleep(1)
    

c = CountdownTask()
t = Thread(target=c.run, args=(10,))
t.start()
# c.terminate() # Signal termination
t.join() # Wait for actual termination (if needed)