def genAscend(numDigits):
    ascend = []
    numbers = '0123456789'
    if numDigits != 0:
        for n in range(10 ** (numDigits - 1), 10 ** numDigits):
            allowed = numbers
            for c in str(n):
                if c in allowed:
                    allowed = allowed[(allowed.find(c) + 1):]
                    continue
                break
            else:
                ascend.append(n)
    return ascend
    
def genDescend(numDigits, upperLimit):
    descend = []
    numbers = '0123456789'
    if numDigits != 0:
        if numDigits == 1:
            descend.append(0)
        for n in range(10 ** (numDigits - 1), 10 ** numDigits):
            allowed = numbers[:numbers.find(str(upperLimit))]
            for c in str(n):
                if c in allowed:
                    allowed = allowed[:allowed.find(c)]
                    continue
                break
            else:
                descend.append(n)
    return descend 

def genTriangle(n):
    triangles = [(i + 1) for i in range(9)]
    if n < 10:
        return triangles[:n]
    count = 10
    length = 1
    while True:
        for upper in genAscend((length - 1) / 2 + 1):
            for lower in genDescend((length - 1) / 2, upper % 10):
                triangles.append(int(str(upper) + str(lower)))
                count += 1
                if count > n:
                    return triangles
        length += 2

