L = range(1, 301)
print L

def alg():
    global L
    x = L[0]
    y = L[1]
    L = L[2:]
    L.append(x * y + x + y)
    L.sort()

while len(L) > 1:
    alg()

print L[0]
print len(str(L[0]))
