def S(n):
    digit = 0
    for i in str(n):
        digit += int(i)
    return n + digit

elements = {}
for i in range(10000):
    temp = S(i)
    if temp in elements:
        elements[temp] += 1
    else:
        elements[temp] = 1
print len(elements)
