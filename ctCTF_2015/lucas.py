alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key1 = "LUCASISAPRETTYCOOLDUDE"
key2 = [11, 20, 2, 0, 18, 8, 18, 0, 15, 17, 4, 19, 19, 24, 2, 14, 14, 11, 3, 20, 3, 4]

def searchfile():
    f = open("note.txt", "r")
    text = f.read()
    count = 0
    output = ""
    for i in range(len(text)):
        if count >= len(test):
            count = 0
        if text[i] == test[count]:
            output += str(i)
            print str(i) + " corresponds to " + text[i]
            count += 1
    f.close()
    f = open("out.txt", "w")
    f.write(output)
    f.close()

def alphatolist(string):
    return [(alpha.index(i)) for i in string]

def listtoalpha(inputlist):
    ans = ""
    for i in inputlist:
        ans += str(i)
    return ans

def vigencrypt(string):
    s = alphatolist(string)
    for i in range(len(s)):
        s[i] = alpha[(s[i] + key2[i % len(key2)]) % 26]
    return listtoalpha(s)

def vigdecrypt(string):
    s = alphatolist(string)
    for i in range(len(s)):
        s[i] = alpha[(s[i] - key2[i % len(key2)]) % 26]
    return listtoalpha(s)

f = open("note.txt", "r")
encode = f.read()
encode = vigencrypt(encode)
f.close()
f = open("lucas.txt", "w")
f.write(encode)
f.close()
