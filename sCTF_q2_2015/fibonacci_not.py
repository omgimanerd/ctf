#! /usr/bin/python

w_table = [0, 1]
for i in range(2, 31):
  w_table.append(w_table[i - 1] * w_table[i - 1] + w_table[i - 2] * w_table[i - 2])
  print i
x = w_table[30]
sum = 0
length = 0
while x >= 10:
  sum += x % 10
  x /= 10
  length += 1
print length, sum

