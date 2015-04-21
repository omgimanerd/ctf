#!/usr/bin/python

f = open('bulbasaur.in', 'r')
moves = []
types = []
hitType = []
damage = []
accuracy = []
moveList = f.read().split('\n')[:-1]
for i in moveList:
  i = i.split(' ')
  moves.append(i[0])
  types.append(i[1])
  hitType.append(i[2])
  damage.append(i[3])
  accuracy.append(i[4])
print moves, types, hitType, damage, accuracy
f.close()
