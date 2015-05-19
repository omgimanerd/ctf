#!/usr/bin/python

import hashlib

def hashDict():
  salt = 'adminadmin'
  fin = open('dict.txt', 'r')
  words = fin.read().split()[::2]
  fin.close()
  fout = open('dict.txt', 'w')
  md5s = []
  for word in words:
    m = hashlib.md5()
    m.update(word + salt)
    md5 = m.hexdigest()
    md5s.append(md5)
    fout.write(word + ' ' + md5 + '\n')
  fout.close()

def attack():
  f = open('dict.txt', 'r')
  ansHash = '571580b26c65f306376d4f64e53cb5c7'
  dictionary = f.read().split('\n')
  for line in dictionary:
    if line != '':
      word = line.split()[0]
      md5 = line.split()[1]
      if md5 == ansHash:
        print word
        print hash
        return 1
  print "No matches found."
  return 0
