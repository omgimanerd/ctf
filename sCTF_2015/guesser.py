#!/usr/bin/python

import socket
import sys

server_address = ('python.sctf.io', 11236)

data = "Nope!"
i = 0
while data == "Nope!":
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  sock.connect(server_address)
  sock.recv(19)
  sock.sendall("1")
  data = sock.recv(20)
  i = i + 1
  print "Attempt #" + str(i)
  print data
  sock.close()
