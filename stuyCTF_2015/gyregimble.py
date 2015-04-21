#!/usr/bin/python

file = open('jabberwocky.txt', 'r')
text = file.read();
file.close()

text = text.split("\n")
t2 = []
for i in text:
  t2.extend(i.split(" "))

print "stuyctf{"+''.join(t2[2::3])+"}"
