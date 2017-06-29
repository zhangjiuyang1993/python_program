#!/usr/bin/env python
#Python3 TCP时间戳客户端

from socket import *

HOST = '127.0.0.1' # or 'localhost'
PORT = 21567
BUFFSIZ = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data = input('> ')
    if not data:
        break
    tcpCliSock.send(data)
    data = tcpCliSock.recv(BUFFSIZ)
    if not data:
        break
    print(data.decode('utf-8'))
tcpCliSock.close()