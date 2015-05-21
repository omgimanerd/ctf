#! /usr/bin/python

from decimal import *
from math import *

def isInt(x):
  return int(x) == x

bottles = Decimal(2506000000000000000)
# sqrt is ~1583035059.624
num = int(ceil(bottles.sqrt()))
while True:
  square = Decimal(num) * Decimal(num)
  disc = (Decimal(8) * square + Decimal(1)).sqrt()
  if isInt(disc):
    print num, square, disc
    break
  if num % 1000 == 0:
    print num, square, disc
  num += Decimal(1)
    
  
