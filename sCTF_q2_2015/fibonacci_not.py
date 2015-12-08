#! /usr/bin/python

goal = 30

w_table = [0, 1]
for i in range(2, goal + 1):
  w_table.append(w_table[i - 1] * w_table[i - 1] + w_table[i - 2] * w_table[i - 2])
  print i
x = str(w_table[goal] * (w_table[goal] - 1))
sum = 0
length = 0
for i in x:
  sum += int(i)
  length += 1
  if length % 500 == 0:
    print sum
print sum, length

