import os
import time

pid = os.fork()
if pid == 0:
    while 1:
        print "helloworld"
        time.sleep(10)
        os._exit(0)

if pid > 0:
    print "parent wait"
    os.waitpid(pid, 0)
    print "parent end"
