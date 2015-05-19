import base64

plainalpha = "abcdefghijklmnopqrstuvwxyz"
rotalpha   = "nopqrstuvwxyzabcdefghijklm"

def rot13(input):
    ans = ""
    for i in input:
        if i in plainalpha:
            ans += rotalpha[plainalpha.index(i)]
        else:
            ans += i
    return ans

def b64(input):
    return base64.b64decode(input)

def cycle(input, iterations):
    string = input
    for i in range(iterations):
        print "Attempt " + str(i)
        string = rot13(string)
        while len(string) % 4 != 0:
            string += "="
        print len(string)
        if i == 4:
            print string
        string = b64(string)
        print string

f = open("persevere.txt", "r")
text = f.read()
cycle(text, 5)
