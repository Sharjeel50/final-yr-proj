from socket import *
import socket
import threading
import sys
import json
import tkinter as tk

#from testdict import a

Final_Chess_Game = __import__("Final Chess Game")

class Server:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    #c1, c2 = False, False
    c1, c2 = None,None


    def __init__(self):
        self.sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        # changed this to localhost (127.0.0.1 when you connect as client) at port 8000
        self.sock.bind(('localhost', 8000))
        self.sock.listen(5)

    def handler(self, c, a):
        while True:
            data = c.recv(1024)
            print("DATA RECIEVED BY THE SOCKET!    ",data)
            if self.c1 != None and self.c2 != None:
                if c == self.c1:
                    print("from c1")
                    self.c2.send(data)
                elif c == self.c2:
                    print("from c2")
                    self.c1.send(data)
                #for connection in self.connections:
                 #   connection.send(data)
                if not data:
                    print(str(a[0]) + ':' + str(a[1]), "connected")
                    #self.connections.remove(c)
                    #c.close()
                    break

    def run(self):
        while True:
            c, a = self.sock.accept()
            cThread = threading.Thread(target=self.handler, args=(c,a))
            cThread.deamon = True
            cThread.start()
            if self.c1:
                print("Client 1 connected")
                self.c2 = c
                print("Client 1 ",self.c1, type(self.c1))

            else:
                print("Client 2 connected")
                self.c1 = c
                print("Client 2,", self.c1, type(self.c1))
            print(str(a[0]) + ':' + str(a[1]), "connected")

#else:
    print("Server started..")
    print("To talk to this server, run this program again in a different terminal")
    print("Use 127.0.0.1 as the parameter after the program to connect to this server (localhost)")
    print("Then you can enter messages and receive them back as bytes, like an echo server")
server = Server()
server.run()
