import math
import re
import socket
import sys
import time

HOST = 'programming.easyctf.com'
PORT = 10300

def quadratic_max_root(a, b, c):
  x1 = (-b + math.sqrt((b * b) - 4 * a * c)) / (2 * a)
  x2 = (-b - math.sqrt((b * b) - 4 * a * c)) / (2 * a)
  return int(max(x1, x2))

def quadratic_min_root(a, b, c):
  x1 = (-b + math.sqrt((b * b) - 4 * a * c)) / (2 * a)
  x2 = (-b - math.sqrt((b * b) - 4 * a * c)) / (2 * a)
  return int(min(x1, x2))

def parseMathBasic(a, op, b):
  if op == '+':
    return a + b
  elif op == '-':
    return a - b
  elif op == 'x':
    return a * b
  print 'You fucked up'

def parseMath(a, op1, b, op2, c, op3, d):
  return parseMathBasic(parseMathBasic(parseMathBasic(
    a, op1, b), op2, c), op3, d)

def findSigns(a, b, c, d, e):
  for i in ['+', '-', 'x']:
    for j in ['+', '-', 'x']:
      for k in ['+', '-', 'x']:
        if parseMath(a, i, b, j, c, k, d) == e:
          return '%s%s%s' % (i, j, k)
  print 'You fucked up'

def solvePhysics(vx, h, a):
  t = math.sqrt(abs(h / (a / 2)))
  return int(vx * t)

def waySplit(s):
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

  return ways[d]

def interpret(data):
  if data.find('Find the value of the greater root') != -1:
    a = int(data.split(' ')[-5].split('x')[0])
    b = int(data.split(' ')[-3][:-1])
    if data.split(' ')[-4] == '-':
      b *= -1
    c = int(data.split(' ')[-1])
    if data.split(' ')[-2] == '-':
      c *= -1
    root = quadratic_max_root(a, b, c)
    return str(root)
  elif data.find('Find the value of the lesser root') != -1:
    a = int(data.split(' ')[-5].split('x')[0])
    b = int(data.split(' ')[-3][:-1])
    if data.split(' ')[-4] == '-':
      b *= -1
    c = int(data.split(' ')[-1])
    if data.split(' ')[-2] == '-':
      c *= -1
    root = quadratic_min_root(a, b, c)
    return str(root)
  elif data.find('Fill the operations (+, -, or x)') != -1:
    a = int(data.split(' ')[-9][3:])
    b = int(data.split(' ')[-7][:-1])
    c = int(data.split(' ')[-5][:-1])
    d = int(data.split(' ')[-3][:-1])
    e = int(data.split(' ')[-1])
    return str(findSigns(a, b, c, d, e))
  elif data.find('projected from the side of a desk') != -1:
    split = data.split(' ')
    vx = int(split[split.index('m/s.') - 1])
    h = int(split[split.index('m') - 1])
    a = 10
    return str(solvePhysics(vx, h, a))
  elif data.find('checkout at') != -1:
    return str(waySplit(data))
  else:
    return str(1)

def main():
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect((HOST, PORT))
  data = s.recv(1024)
  data = s.recv(1024)
  print data
  answer = interpret(data)
  s.sendall(answer)
  data = s.recv(1024)
  if data.find('incorrect') != -1:
    print data
    sys.exit(0)
  else:
    print 'Correct answer: %s\n' % answer

  while True:
    data = s.recv(1024)
    print "Next problem: " + data
    if data.find('flag') != -1:
      print data
      break
    answer = interpret(data)
    s.sendall(answer)
    data = s.recv(1024)
    if data.find('incorrect') != -1:
      print data
      break
    else:
      print data
      print 'Correct answer: %s\n' % answer

if __name__ == '__main__':
  main()
