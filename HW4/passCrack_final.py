# Praakrit Pradhan
# Computer Engineering
# Cloud Computing
# Universtiy of Cincinnati
#!/usr/bin/env python

# Problem Statement: Password cracking - passCrack.py - Given a string of characters on the command line, find what string hashes to it.  Passwords are sometimes stored in a hashed form, so if the database is breached, the passwords are not easily usable. For this assignment, assume we have a hash of a password in hex form.  Given this hash on the command line, find what password hashes to it.  Only the first 5 characters of the hash are checked.  Assume passwords are 4 or fewer characters containing only lowercase letters and numbers.  Use MapReduce to quickly look through all combinations for a match.  Print out the input hash string and the valid passwords which hash to it, if any.  Use hashlib md5 hexdigest()and use the first 5 characters.  Here are some passwords to crack: d077f, 0832c, 1a1dc, ee269, 0fe63
# Example:
# hash_object = hashlib.md5(b'Hello World')
# print(hash_object.hexdigest())

import mincemeat
import sys
import hashlib
# import digits and ascii_lowercase for making the combinations
from string import digits, ascii_lowercase
# import product for fast run through combinations
from itertools import product

# setup charz as all the digits and ascii_lowercase
chars = digits + ascii_lowercase
# setup size as total size/60 , cuz 60 is fun
siz = (36**4 + 36**3 + 36**2 + 36)/60 + 1
# take in hash key inputted in command line
hash_in = sys.argv[-1]
# setup empty lists
data = []
# setup empty list : with the input(so you can pass it in all the time)
lst = [hash_in]
# -> Code I took reference from :
# # http://stackoverflow.com/questions/464864/python-code-to-pick-out-all-possible-combinations-from-a-list
# # for n in itertools.count():
# #        for t in itertools.product(string.ascii_letters + string.digits, repeat=n):
# #            yield ''.join(t)

# setup count
count = 0
# code example for different combinations of letters and numbers
for n in range(1, 4 + 1):
    for charz in product(chars, repeat=n):
        # print charz #: was used for checking \nu
        something = ''.join(charz)
        lst.append(something)
        count += 1
        # check if reached size
        if count >= siz:
            # append to main data
            data.append(lst)
            # reset initializer
            lst = [hash_in]
            count = 0
# final append
data.append(lst)
datasource = dict(enumerate(data))

# Just to show whats being checked
print 'Attacking --->',hash_in

# start mapfn
def mapfn(k, v):
    # print() #: was used /nu
    # pop out the first number (which is the hashed input)
    numeroUno = v.pop(0)
    # start checking each other number
    for num in v:
        new = hashlib.md5(num).hexdigest()[0:5]
        if new == numeroUno:
            # if number after hashing is the same, yield
            yield 'Found',num
# end mapfn
# start reducefn
def reducefn(k, vs):
    # print('reducefn') #: for checking /nu
    # print(k,vs) #: for chekcing
    return vs
# end reducefn

# server setup stuff for map/reduce
s = mincemeat.Server()
s.datasource = datasource
s.mapfn = mapfn
s.reducefn = reducefn

# pulling out all results
results = s.run_server(password="changeme")
# printing the final results
print results
