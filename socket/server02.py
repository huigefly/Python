#!/usr/bin/env python

import SocketServer
from time import ctime
import time

HOST = ''
PORT = 21566
ADDR = (HOST, PORT)

class MyRequestHandler(SocketServer.StreamRequestHandler):
    def handle(self):
        print '...connected from:', self.client_address
        self.wfile.write('[%s] %s\n' % (
            ctime(), self.rfile.readline().strip())
        )
        time.sleep(100)

# tcpSerSock = SocketServer.ThreadingTCPServer(ADDR, MyRequestHandler)
SocketServer.ForkingTCPServer.allow_reuse_address = True
tcpSerSock = SocketServer.ForkingTCPServer(ADDR, MyRequestHandler)
print 'waiting for connection...'
tcpSerSock.serve_forever()
