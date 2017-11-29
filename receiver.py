#!/usr/bin/env python
import socket

# TCP_IP = '127.0.0.1'
TCP_PORT = 40000
BUFFER_SIZE = 20  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', TCP_PORT))
s.listen(1)

conn, addr = s.accept()
print 'Connection address:', addr
while 1:
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    if data == "s":
    	print "received start"
    elif data == "e":
    	print "received end"
    conn.send("data")  # echo
conn.close()

#!/usr/bin/env python

# import socket


# TCP_IP = '128.205.28.87'
# TCP_PORT = 23
# BUFFER_SIZE = 1024
# MESSAGE = "Hello, World!"

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# print "ready to connect"
# s.connect((TCP_IP, TCP_PORT))
# print "connected"
# s.send(MESSAGE)
# data = s.recv(BUFFER_SIZE)
# s.close()

# print "received data:", data