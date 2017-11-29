#!/usr/bin/env python

from time import sleep
import socket


TCP_IP = '127.0.0.1'
TCP_PORT = 40000
BUFFER_SIZE = 1024
MESSAGE = "s"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

# while True:
s.send(MESSAGE)
data = s.recv(BUFFER_SIZE)
# print "received data:", data
# sleep(0.5)

s.close()