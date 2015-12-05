#! /usr/bin/python

import socket
import re
import math

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('programming.easyctf.com', 10300)
sock.connect(addr)

while True:
  s = sock.recv(1024)
  ans = ''
  if s == '':
    print 'Done!'
    break
  else:
    print s
  if 'root' in s:
    r = s[s.find('root') + 6:]
    m = re.match('(\d+)[^+-]*([+-] \d+)[^+-]*([+-] \d+)', r)
    a = int(m.group(1))
    b = int(m.group(2))
    c = int(m.group(3))
    if 'greater' in s:
      ans = str(int((-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)))
    elif 'lesser' in s:
      ans = str(int((-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)))
  elif 'blanks' in s:
    r = s[s.find('((('):]
    m = re.match('\(\(\(([+-]?\d+) _ ([+-]?\d+)\) _ ([+-]?\d+)\) _ ([+-]?\d+)\) = ([+-]?\d+)', r)
    a = [int(i) for i in m.groups()]
    ops = {'+': lambda x, y: x + y,
           '-': lambda x, y: x - y,
           'x': lambda x, y: x * y}
    for i in ops:
      if ans != '':
        break
      for j in ops:
        if ans != '':
          break
        for k in ops:
          if ans != '':
            break
          if ops[k](ops[j](ops[i](a[0], a[1]), a[2]), a[3]) == a[4]:
            ans = i + j + k
  elif 'checkout' in s:
    r = s[s.find('make') + 6:]
    m = re.match('(\d+\.\d+) using just ([^?]+)?', r)
    d = int(round(float(m.group(1)) * 100))
    c = re.split(', (?:and )?', m.group(2))
    
    coins = {'pennies': 1,
             'nickels': 5,
             'dimes': 10,
             'quarters': 25,
             'dollar bills': 100,
             'five-dollar bills': 500,
             'ten-dollar bills': 1000}
    inc = []
    for i in c:
      inc += [coins[i]]
    inc = sorted(inc)
    ways = [1]+[0] * d
    for c in inc:
      for i in range(c, d + 1):
        ways[i] += ways[i - c]
    
    ans = str(ways[d])
  elif 'projected' in s:
    r = s[s.find('velocity') + 12:]
    m = re.match('(\d+)[^^\d]+(\d+)[^^\d]+(\d+)[^^\d]+(\d+)', r)
    v = int(m.group(1))
    y = int(m.group(2))
    mass = int(m.group(3))
    g = int(m.group(4))
    ans = str(int(v * math.sqrt(2 * y / g)))
  if ans != '':
    print ans
    sock.sendall(ans)

            
        
