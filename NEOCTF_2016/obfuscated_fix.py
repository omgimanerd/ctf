#! /usr/bin/python

num = []
num2 = 0
word = []
word2 = 'My naMk Rs {jamEa} and I {ikq gEttiag obfusc}rted cu{e!'
while (num2 < 11):
    num.append(num2)
    word.append(word2[num2+5])
    num2 += 1

print num
print word
print ''.join([chr(72),chr(ord('e')),'e','_'])

s = 'flag{REkxxxxxxHee_fllaagg}'
y = ''.join(s)
s = list(s)
print ''.join(s[14:18]) 

if len(s) > 26:
    print 'rekt1'
elif ''.join(s[18::2]) != 'flag':
    print 'rekt2'
elif s.pop() != '}':
    print 'rekt3'
elif ''.join(s[0:4]) != 'flag':
    print 'rekt4'
elif 'a'.join(s[len(s)-6::2]) != 'laaag':
    print 'a'.join(s[len(s)-6::2])
    print 'rekt5'
elif ''.join(s[4:8]) != '{REk':
    print 'rekt6'
elif ''.join(s[14:18]) != ''.join([chr(72),chr(ord('e')),'e','_']):
    print 'rekt7'
elif ''.join(s[8:14])!='t_1s_t': 
    print 'rekt8'
else:
    print 'FLAG IS ' + y
