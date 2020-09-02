# -*- coding: utf-8 -*-
import json
from test import Transmit
from test.ttypes import *
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
import socket


class TransmitHandler:
    def __init__(self):
        self.log = {}

    def sayMsg(self, msg, type):
#        msg = json.loads(msg)
        msg = msg
        print("sayMsg(" + msg + type  + ")")
        return "say " + msg + " from " + socket.gethostbyname(socket.gethostname())

    def invoke(self,cmd,token,data):
        cmd = cmd
        token =token
        data = data
        if cmd ==1:
            return json.dumps({token:data})
        else:
            return 'cmd no match'

if __name__=="__main__":
    handler = TransmitHandler()
    processor = Transmit.Processor(handler)
    transport = TSocket.TServerSocket('127.0.0.1', 9090)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()
    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)
    print("Starting python server...")
    server.serve()
