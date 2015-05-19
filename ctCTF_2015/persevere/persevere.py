#!/usr/bin/python

import base64

plainalpha = "abcdefghijklmnopqrstuvwxyz"
rotalpha   = "nopqrstuvwxyzabcdefghijklm"

def rot13(text):
    ans = ""
    for i in text:
        if i in plainalpha:
            ans += rotalpha[plainalpha.index(i)]
        else:
            ans += i
    return ans

b64Values = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '/']

def b64(text):
    binary = ''
    for i in text:
        binary += '0' + str(bin(ord(i)))[2:]

    message = ""
    while binary != '':
        message += b64Values[int(binary[:6], 2)]
        binary = binary[6:]
    return message

def cycle(string, iterations):
    for i in range(iterations):
        string = rot13(string)
        #while len(string) % 3 != 0:
        #    string += "="
        string = base64.urlsafe_b64decode(string)
        print string
        if string.find('flag') != -1:
            return string
    return string

f = open("cipher.txt", "r")
text = f.read()
print cycle(text, 15)
