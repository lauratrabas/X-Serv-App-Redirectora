#!/usr/bin/python
#-*- coding: utf-8 -*-

#Laura Trabas Clavero

import socket
import random

class webApp:

    def parse(self, request):

        return None

    def process(self, parsedRequest):

        return ("200 OK", "<html><body><h1>It works!</h1></body></html>")

    def __init__(self, hostname, port):

    	mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        mySocket.bind((hostname, port))


        mySocket.listen(5)


        while True:
            print 'Waiting for connections'
            (recvSocket, address) = mySocket.accept()
            print 'HTTP request received (going to parse and process):'
            request = recvSocket.recv(2048)
            print request
            parsedRequest = self.parse(request)
            (returnCode, htmlAnswer) = self.process(parsedRequest)
            print 'Answering back...'
            recvSocket.send("HTTP/1.1 " + returnCode + " \r\n\r\n"
                            + htmlAnswer + "\r\n")
            recvSocket.close()

class aleatApp(webApp):
    def process(self, parsedRequest):
        numero = random.randint(0, 10000000000000)
        respuesta ="<html><body>" + '<meta http-equiv="refresh" content="0;url=http://localhost:1234"/>' + "</head><html>" + "\r\n"

        return ("302 Found", respuesta)

if __name__ == "__main__":
    testWebApp = aleatApp("localhost", 1234)
