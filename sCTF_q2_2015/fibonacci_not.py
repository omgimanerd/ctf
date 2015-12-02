#! /usr/bin/python

w_table = [0, 1]
for i in range(2, 31):
  w_table.append(w_table[i - 1] * w_table[i - 1] + w_table[i - 2] * w_table[i - 2])
  print i
print w_table[30] * (w_table[30] - 1)

