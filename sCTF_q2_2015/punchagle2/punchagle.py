import Image
import ImageChops
import os
import re

imgPath = os.getcwd() + '/images/'
imgDataPath = os.getcwd() + '/images_data/'

def atoi(s):
    return int(s) if s.isdigit() else s

def naturalKey(s):
    return [atoi(c) for c in re.split('(\d+)', s)]

def convert(img):
    paths = os.listdir(imgDataPath)
    for i in range(len(paths)):
        datum = Image.open(imgDataPath + paths[i])
        if ImageChops.difference(img, datum).getbbox() is None:
            return i
    return 'x'

def process(img):
    region = img.crop((0, 40, img.size[0], img.size[1] - 9))
    rowTot = region.size[1] / 20
    rows = []
    for rowNum in range(rowTot + 1):
        rowReg = region.crop((region.size[0] / 2 - 15 - 10 * rowNum,
                              rowNum * 20,
                              region.size[0] / 2 + 16 + 10 * rowNum,
                              rowNum * 20 + 11))
        syms = []
        symTot = rowNum + 2
        for symNum in range(symTot):
            symReg = rowReg.crop((20 * symNum, 0, 20 * symNum + 11, 11))
            syms.append(symReg)
        rows.append(syms)
    return rows

def calcStr():
    images = sorted(os.listdir(imgPath), key=naturalKey)
    output = ''
    for path in images:
        img = Image.open(imgPath + path)
        imgObjs = process(img)
        for imgObjRow in imgObjs:
            for imgObj in imgObjRow:
                output += str(convert(imgObj))
    open('images.out', 'w+').write(output)

def findFlag():
    s = open('images.out', 'r').read()
    match = ''.join([''.join(['[' + j + 'x]' for j in str(ord(i))]) for i in 'sctf{'])
    print match
    m = re.match(match, s)
    print m
    end = start + s[start:].find(str(ord('}'))) + 3
    dec = s[start:end]
    out = ''
    i = 0
    while i < len(dec):
        num = ''
        if dec[i] > '1':
            num += dec[i:i + 2] + ' '
            i += 2
        else:
            num += dec[i:i + 3] + ' '
            i += 3
        out += chr(int(num))
    print out
    open('flag.txt', 'w+').write(out)

calcStr()
findFlag()
        
