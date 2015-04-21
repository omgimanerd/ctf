#!/usr/bin/python

f1 = open('jabberwocky1.txt', 'r')
f2 = open('jabberwocky2.txt', 'r')
s1 = f1.read().split()
s2 = f2.read().split()
for i in range(3):
  print 'stuyctf{' + ''.join(s1[i::3]) + '}\n'
  print 'stuyctf{' + ''.join(s2[i::3]) + '}\n'
f1.close()
f2.close()
