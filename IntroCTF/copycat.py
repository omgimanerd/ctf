#!/usr/bin/python

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('introctf.me', 33333))
print s.recv(1024)
for i in range(100):
    if i % 3 == 0:
        s.sendall('p\n')
    elif i % 3 == 1:
        s.sendall('s\n')
    else:
        s.sendall('r\n')
    print s.recv(1024)
print s.recv(1024)
s.close()
