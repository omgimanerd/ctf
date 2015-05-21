#! /usr/bin/python

from decimal import *
import sys
import time


limit = Decimal(sys.argv[1])

def isInt(n):
  return int(n) == float(n)

i = Decimal(1)
sum = 0
while i <= limit:
  hypotenuse = (i * i + (i + 1) * (i + 1)).sqrt()
  if isInt(hypotenuse):
    sum += i
    print i, i + 1, hypotenuse, sum
  i += 1
  time.sleep(0)
  
