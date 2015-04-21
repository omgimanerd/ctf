#!/usr/bin/python2.7
import os
import time
alp = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

types = ['aes-128-cbc', 'aes-128-ecb', 'aes-192-cbc', 'aes-192-ecb', 'aes-256-cbc', 'aes-256-ecb', 'base64', 'bf', 'bf-cbc', 'bf-cfb', 'bf-ecb', 'bf-ofb', 'camellia-128-cbc', 'camellia-128-ecb', 'camellia-192-cbc', 'camellia-192-ecb', 'camellia-256-cbc', 'camellia-256-ecb', 'cast', 'cast-cbc', 'cast5-cbc', 'cast5-cfb', 'cast5-ecb', 'cast5-ofb', 'des', 'des-cbc', 'des-cfb', 'des-ecb', 'des-ede', 'des-ede-cbc', 'des-ede-cfb', 'des-ede-ofb', 'des-ede3', 'des-ede3-cbc', 'des-ede3-cfb', 'des-ede3-ofb', 'des-ofb', 'des3', 'desx', 'idea', 'idea-cbc', 'idea-cfb', 'idea-ecb', 'idea-ofb', 'rc2', 'rc2-40-cbc', 'rc2-64-cbc', 'rc2-cbc', 'rc2-cfb', 'rc2-ecb', 'rc2-ofb', 'rc4', 'rc4-40', 'seed', 'seed-cbc', 'seed-cfb', 'seed-ecb', 'seed-ofb', 'zlib']
print len(types)
def decrypt(encryptedfile, storagefile, pot):
        for t in pot:
                for i in alp:
                        for j in alp:
 #                               os.system("printf " + i+j+" |  openssl "+t+" -in " + encryptedfile + " -out " + storagefile + " -pass stdin")
                                os.system("printf " + i+j+" |  openssl "+t+" -d -in " + encryptedfile + " -out " + storagefile + " -pass stdin")
                                target = open(storagefile, "r").read()
                                #print target
                                #time.sleep(.5)
                                if target.find("stuyctf") != -1:
                                        print  target
                                        print t
                                        print i+j
                                        break 
                
                
enc = "secret.txt"
store = "store.txt"

decrypt(enc, store, types)
