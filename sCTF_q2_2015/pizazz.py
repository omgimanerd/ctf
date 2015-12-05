#! /usr/bin/python

import subprocess

enc = '221.164.100.10.237.97.167.177.205.54.30.53.124.232.78.134.215.10.37.45.30.244.131.235.116.131.237.237.85.27.210.205.35.76.5.5.210.102.157.157.3.96.114.25.91.238.192.'

nums = [int(n) for n in enc.split('.')[:-1]]

charset = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-_{}'

ans = 'flag'

for i in range(4, len(nums)):
  for c in charset:
    if subprocess.check_output('./pizazz ' + ans + c, shell=True)[:-1] in enc:
      ans += c
      break

print ans
