#!/usr/bin/python

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ '
passphrase = 'LUCAS IS A PRETTY COOL DUDE'

def vigenc(plain, key):
  result = ""
  for i in range(len(plain)):
    plainindex = alphabet.index(plain[i])
    keyindex = alphabet.index(key[i % len(key)])
    result += alphabet[(plainindex + keyindex) % len(alphabet)]
  return result

def vigdec(cipher, key):
  result = ""
  for i in range(len(cipher)):
    cipherindex = alphabet.index(cipher[i])
    keyindex = alphabet.index(key[i % len(key)])
    result += alphabet[(cipherindex - keyindex) % len(alphabet)]
  return result

def solve():
  f1 = open('note.txt', 'r')
  s = vigdec(f1.read(), passphrase)
  f2 = open('out.txt', 'w')
  f2.write(s)
  f1.close()
  f2.close()

solve()
