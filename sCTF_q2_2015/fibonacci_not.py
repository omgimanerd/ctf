#! /usr/bin/python

g_table = [0, 1]
w_table = [0, 1]
for i in range(2, 31):
  g_table.append((g_table[i - 1] + g_table[i - 2]) * (g_table[i - 1] + g_table[i - 2]))
  w_table.append(w_table[i - 1] * w_table[i - 1] + w_table[i - 2] * w_table[i - 2])
  print i
print g_table[30] - w_table[30]
