import sys
import random
import string

blarg = raw_input("_")

def foo(plain, offset):
 alpha = string.ascii_lowercase
 new = alpha[offset:] + alpha[:offset]
 trans = string.maketrans(alpha, new)
 return plain.translate(trans)

def main(argv):
 print foo(blarg,15)
 if foo(blarg,15)==foo("iwtuapvxhgxedqujhrpit", 26):
  print "yay!"
  print sys.argv[1]
 else:
  print "aww."
main(sys.argv)
