#!/usr/bin/python

import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('python.sctf.io', 11234)

sock.connect(server_address)

try:
  print sock.recv(50)
  sock.sendall("5")
  print sock.recv(50)
  
finally:
  sock.close()
