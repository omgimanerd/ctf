#!/usr/bin/python

f = open('slashes.txt', 'r')
data = f.read()
length = len(data)
s = ""

for i in range(length / 8):
  s += chr(int(data[i * 8: i * 8 + 7], 2))
f.close()
print s
