# Password cracking - passCrack.py - Given a string of characters on the command line, find what string hashes to it.  Passwords are sometimes stored in a hashed form, so if the database is breached, the passwords are not easily usable. For this assignment, assume we have a hash of a password in hex form.  Given this hash on the command line, find what password hashes to it.  Only the first 5 characters of the hash are checked.  Assume passwords are 4 or fewer characters containing only lowercase letters and numbers.  Use MapReduce to quickly look through all combinations for a match.  Print out the input hash string and the valid passwords which hash to it, if any.  Use hashlib md5 hexdigest()and use the first 5 characters.  Here are some passwords to crack: d077f, 0832c, 1a1dc, ee269, 0fe63

# Example:
# hash_object = hashlib.md5(b'Hello World')
# print(hash_object.hexdigest())

#!/usr/bin/env python
import mincemeat
import sys
import hashlib

from string import digits, ascii_lowercase
from itertools import product

chars = digits + ascii_lowercase

hash_in = sys.argv[-1]
print(hash_in)
data = {} 
#setting up my breh as dictionary
for n in range(1, 2 + 1):
    for charz in product(chars, repeat=n):
        data[''.join(charz)]=hash_in

# print(data)

datasource = data

print 'Attacking --->',hash_in
def mapfn(k, v):
    # print()
    new = hashlib.md5(k).hexdigest()[0:5]
    if new == v:
        print(new,k)
        yield new,k

def reducefn(k, vs):
    print('reducefn')
    print(k,vs)

    return vs

s = mincemeat.Server()
s.datasource = datasource
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")
print results
