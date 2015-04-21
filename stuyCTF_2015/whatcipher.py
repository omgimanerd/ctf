#!/usr/bin/python2.7
import os

alp = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def decrypt(encryptedfile, storagefile):
        for i in alp:
                for j in alp:
                        os.system("printf " + i+j+" |  openssl aes-128-cbc -in " + encryptedfile + " -out " + storagefile + " -pass stdin")
                        target = open(storagefile, "r").read()
                        print target
                        #if target.find("") != -1:
#                                print target
                
                
enc = "/Users/radhikajha/Desktop/secret.txt"
store = "/Users/radhikajha/Desktop/store.txt"

decrypt(enc, store)
