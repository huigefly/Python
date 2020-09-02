#!/usr/bin/env python

from SocketServer import TCPServer, ThreadingTCPServer, StreamRequestHandler
from time import ctime
import time
from bt_constant import *

class MsgTransfer(StreamRequestHandler):
    def handle(self):
        print '...connected from:', self.client_address
        self.wfile.write('[%s] %s\n' % (
            ctime(), self.rfile.readline().strip())
        )
        print ("recv 0:%s" % self.rfile.readline().strip())
        print ("recv 1:%s" % self.rfile.readline().strip())

if __name__ == "__main__":
    TCPServer.allow_reuse_address = True
    tcpSerSock = ThreadingTCPServer(ADDR, MsgTransfer)
    # tcpSerSock = ForkingTCPServer(ADDR, MyRequestHandler)
    print 'waiting for connection...'
    tcpSerSock.serve_forever()
