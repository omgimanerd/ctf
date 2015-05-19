import binascii

asciistr = "not a hash lol  "
asciilist   = ["n",  "o",  "t",  " ",  "a",  " ",  "h",  "a",  "s",  "h",  " ",  "l",  "o",  "l",  " ",  " " ]
plainhex    = ["6e", "6f", "74", "20", "61", "20", "68", "61", "73", "68", "20", "6c", "6f", "6c", "20", "20"]
cipherhex   = ["32", "1a", "12", "4c", "27", "4c", "70", "27", "39", "70", "4c", "18", "1a", "18", "4c", "4c"]
plainalpha  = ["6e", "6f", "74", "20", "61", "68", "73", "20", "6c"]
cipheralpha = ["32", "1a", "12", "4c", "27", "70", "39", "4c", "18"]

ciphered1   = ["27", "62", "3b", "1c", "6b", "18", "18", "1f", "ed", "12", "2b", "11", "30", "27", "11", "1f"]
ciphered2   = ["cb", "cb", "38", "1b", "20", "3b", "23", "22", "33", "cb", "cb"]

def strtolist(inputstring):
    list = [inputstring[(2 * i):(2 * i + 2)] for i in range(len(inputstring)/2)]
    return list

def listtostr(inputlist):
    string = ""
    for i in inputlist:
        string += str(i)
    return string

def cipher(plaintext):
    ciphered = plaintext
    for i in range(len(ciphered)):
        if ciphered[i] in plainalpha:
            ciphered[i] = cipheralpha[plainalpha.index(ciphered[i])]
    return ciphered

def decipher(ciphertext):
    deciphered = ciphertext
    undeciphered = []
    for i in range(len(deciphered)):
        if deciphered[i] in cipheralpha:
            deciphered[i] = plainalpha[cipheralpha.index(deciphered[i])]
        else:
            if not deciphered[i] in undeciphered:
                undeciphered.append(deciphered[i])
            deciphered[i] = str(0x1f + int(str(undeciphered.index(str(deciphered[i]))), 16))
    return deciphered

print binascii.unhexlify(listtostr(decipher(ciphered1)))
print binascii.unhexlify(listtostr(decipher(ciphered2)))
