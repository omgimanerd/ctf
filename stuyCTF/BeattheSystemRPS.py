#!/usr/bin/python

import random
import socket

def rps():
    global ans
    while len(ans)<200:
        length = len(ans)
        if len(ans) >= 10:
            test = -10
        else:
            test = -len(ans)
        while test < 0:
            mem = ans[test:]
            if ans[:-1].find(mem) != -1:     #If the string exists besides the newest
                i = ans[:-1].find(mem)       #Always will, since mem can go down to 1 char
                prevC = ans[i-test]
                rs = mem + "r"
                ps = mem + "p"
                ss = mem + "s"
                rc = ans[:-1].count(rs)
                pc = ans[:-1].count(ps)
                sc = ans[:-1].count(ss)
                stringList = [rs, ps, ss]
                countList = [rc, pc, sc]
                num = stringList[countList.index(max(countList))][-1:]
                
                if num == "r":
                    ans += "s"
                    test = 0
                elif num == "p":
                    ans += "r"
                    test = 0
                elif num == "s":
                    ans += "p"
                    test = 0
            else:
                if test == -1:
                    print test
                test += 1
        
def fix():
    global ans
    i = 1
    while i < 600:
        ans = ans[:i] + "\\n" + ans[i:]
        i += 3


address = ('stuyctf.me', 50000)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(address)


#do it manually for the first four. Then update ans accordingly
print s.recv(1024)
s.sendall("RockBeatsScissorsBeatsPaper\n")
print s.recv(1024)

i = 0
ans = ""
while i < 8:
    x = random.randrange(0,1000)
    if x % 3 == 0:
        ans += "r"
    elif x % 3 == 1:
        ans += "p"
    else:
        ans += "s"
    i += 1

rps()
print ans

for i in ans:
    print s.recv(1024)
    s.send(i + "\n")
    print s.recv(1024)

s.close()
    
