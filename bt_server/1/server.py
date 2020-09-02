#!/usr/bin/env python

from SocketServer import TCPServer, ThreadingTCPServer, StreamRequestHandler, ForkingTCPServer
from time import ctime
import time
from constant import *

class MsgTransfer(StreamRequestHandler):

    def handle(self):
        print("addr is :",self.client_address) # addr

        while True:
            try:
                data = self.request.recv(1024).strip()
                if not data: break
                if data == "make_torrent":
                    print(" server ready make torrent")
                    '''
                    make_torrent()
                    blocking
                    '''
                elif data == "download":
                    print(" server download")
                    '''
                    libtorrent add param ....
                    add_handle()
                    no block
                    '''
                elif data == "seeding":
                    '''
                    start seeding ..
                    no block
                    '''
                    print("start seeding")

                print("recv from client:",data)
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
