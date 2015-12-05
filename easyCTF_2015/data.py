#! /usr/bin/python

import os
import binascii

fs = os.listdir('data/')
for s in fs:
  with open('data/' + s, 'r') as f:
    if ('d8ff' in binascii.hexlify(f.read())):
      print s
      break
