#!/usr/bin/python

import sys
import math
import struct

p = lambda x: struct.pack('b', x)
u = lambda x: struct.unpack('f', x)[0]

if len(sys.argv) != 4:
    sys.exit(1)

filename = sys.argv[1]
keyx = int(sys.argv[2])
keyy = int(sys.argv[3])

print "(%d, %d)" % (keyx, keyy)

enc = open(filename + '.enc' , 'rb').read()
ans = open(filename + '.out', 'w')

for r in range(100):
    print 'r = ' + str(r)
    ans.write('\nr = ' + str(r) + '\n')
    for i in range(0, len(enc) - 7, 8):
        x, y = u(enc[i:i+4]), u(enc[i+4:i+8])
        print x, y
        try:
            ans.write(p((int(round(((r ** 2) * x) / (x ** 2 + y ** 2))) + 128) % 256 - 128) + p((int(round(((r ** 2) * y) / (x ** 2 + y ** 2))) + 128) % 256 - 128))
        except ZeroDivisionError:
            ans.write(p((int(round(x)) + 128) % 256 - 128) + p((int(round(y)) + 128) % 256 - 128))
ans.close()
