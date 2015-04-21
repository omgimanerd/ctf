#!/usr/bin/python

import sys
import math
import struct

p = lambda x: struct.pack('f', x)
u = lambda x: struct.unpack('f', x)[0]

if len(sys.argv) != 3:
    sys.exit(1)

filename = sys.argv[1]
# key: 141975642814
key = math.radians(int(sys.argv[2]))

print key

enc = open(filename + '.enc', 'rb').read()
ans = open(filename + '.out', 'wb')

# x cos(key) - y sin(key) = a
# x sin(key) + y cos(key) = b

# x = a cos(key) + b sin(key)
# y = b cos(key) - a sin(key)

for i in range(0, len(enc), 8):
    a, b = u(enc[i:i+4]), u(enc[i+4:i+8])
    x = int(round(a * math.cos(key) + b * math.sin(key))) % 128
    y = int(round(b * math.cos(key) - a * math.sin(key))) % 128
    print "x = " + str(x) + ", y = " + str(y)
    ans.write(chr(x) + chr(y))

ans.close()

