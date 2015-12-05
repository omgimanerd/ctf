#! /usr/bin/python

from itertools import product

key = 3

def encrypt(message):
  encrypted = ' '.join([str(ord(c) // key) for c in message])
  return encrypted

def decrypt(message):
  decrypted1 = ' '.join([chr(int(c) * key) for c in message.split(' ')])
  decrypted2 = ' '.join([chr(int(c) * key + 1) for c in message.split(' ')])
  decrypted3 = ' '.join([chr(int(c) * key + 2) for c in message.split(' ')])
  return [decrypted1, decrypted2, decrypted3]

enc = open('floors.txt', 'r').read()
print '\n'.join([s for s in decrypt(enc)])
a = [s.split(' ')[-9:] for s in decrypt(enc)]
for i0, i1, i2, i3, i4, i5, i6, i7, i8 in product(range(3), range(3), range(3), range(3), range(3), range(3), range(3), range(3), range(3)):
  s = a[i0][0] + a[i1][1] + a[i2][2] + a[i3][3] + a[i4][4] + a[i5][5] + a[i6][6] + a[i7][7] + a[i8][8];
  print s
