#!/usr/bin/env python

from SocketServer import TCPServer, ThreadingTCPServer, StreamRequestHandler, ForkingTCPServer
from time import ctime
import time
from constant import *
from msg_handle_factory import MsgHandleFactory

class MsgTransfer(StreamRequestHandler):

    def handle(self):
        print("addr is :",self.client_address) # addr

        while True:
            try:
                # data : xml; json; define format; so on
                data = self.request.recv(BUF_SIZE).strip()
                if not data: break
                print("recv from client:%s" % data)
                # think param input
                # do not block msg 
                msg_tyep = data.split('#')
                obj = MsgHandleFactory.get(msg_tyep[0])
                obj.init(data)
                obj.run()
                obj.response()
                self.request.sendall(data.upper())
            except Exception as e:
                print(e)
                break

if __name__ == "__main__":

    

    TCPServer.allow_reuse_address = True
    # tcpSerSock = ThreadingTCPServer(ADDR, MsgTransfer)
    tcpSerSock = ForkingTCPServer(ADDR, MsgTransfer)
    print 'waiting for connection...'
    tcpSerSock.serve_forever()
