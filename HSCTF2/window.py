#! /usr/bin/python

from decimal import *
import sys
import time

def genPell(n):
  pell = [0, 1]
  if n in [1, 2]:
    return pell[:(n - 1)]
  for i in range(2, n):
    pell.append(2 * pell[i - 1] + pell[i - 2])
  return pell

def genTriples(n):
  pell = genPell(int((n / 2) ** 0.5))
  count = 0
  for i in range(1, len(pell)):
    pell1 = pell[i]
    pell2 = pell[i + 1]
    triple = sorted([pell2 * pell2 - pell1 * pell1, 2 * pell1 * pell2, pell1 * pell1 + pell2 * pell2])
    print triple
    if triple[1] >= n:
      break
    count += triple[0]
  print count
    
genTriples(9999999997)
