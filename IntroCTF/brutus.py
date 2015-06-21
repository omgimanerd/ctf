import hashlib
import re

words = open('20k.txt', 'r').read().split('\n')[:-1]
soln = '66ad2dced84182ab686bb60e00fbc7fd'
#soln = '98af68859b0b92a8eb96b70ea6247338'

for word in words:
    for num in range(1000, 10000):
        if hashlib.md5(word + str(num)).hexdigest() == soln:
            print word + str(num)
            break
    else:
        continue
    break
        
