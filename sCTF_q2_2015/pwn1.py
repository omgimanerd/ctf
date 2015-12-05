#! /usr/bin/python

import socket

host = 'pwn.problem.sctf.io'
port = 1337

for i in range(42):
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect((host, port))
  s.sendall('A' * i + '\n')
  print s.recv(1024)
  s.close()
