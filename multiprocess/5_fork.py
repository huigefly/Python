#!/usr/bin/python2.7

import os
import time
from logging import getLogger
logger = getLogger()
g_value = 10

try:
    pid = os.fork()
    if pid == 0:
        while 1:
            logger.info("i am child")
            g_value = g_value -1
            print g_value
            time.sleep(10)
            os._exit(0)

    if pid > 0:
        logger.info("parent wait here")
        os.waitpid(pid, 0)
        logger.info("parent end")

except OSError, e:
    print ("system error fork")