# Praakrit Pradhan
# Computer Engineering
# Cloud Computing
# Universtiy of Cincinnati
#!/usr/bin/env python
# Problem Statement: Find palindrome prime numbers from 2 -> 10000000
import mincemeat
import sys
# /nu => not used
# import line_profiler #: was done for speed checks /nu

# siz = 10000 : initial check for size
# size for grouping, again 60 a decent number
siz = 10000000/60 + 2
# empty lists to group up the big data
data = []
lit = []
# grouping data
# ***Going from 2-10Mil (will not print 0 or 1)***
for i in range(2,10000000):
    lit.append(i)
    if len(lit)==siz:
        data.append(lit)
        lit = []
# final append so we dont miss the last bit
data.append(lit)
datasource = dict(enumerate(data))
# print data #: was done for checking grouping /nu

# start mapfn
def mapfn(k, v):
    import math
    # start isPrime
    def isPrime(v):
        flag = 1
        # print v,'isPrime' #: done for checking /nu
        for i in (range(2,((int(math.ceil(math.sqrt(v))))+1))):
            if ((v % i) is 0):
                flag = 0
                break
        # print flag,'after prime check' #: dont for checks /nu
        return flag
    # end isPrime
    # Going through input of v, iterating through the groups
    for i in v:
        # 2 is a prime/and pali yield right away.
        if (i is 2):
            yield 'PaliPrimes',int(i)
        # check for none of multiples of 2,3,5,or 7 : quick removal of bunch of data
        if ((i % 2) is not 0) or ((i % 3) is not 0) or ((i % 5) is not 0) or ((i % 7) is not 0):
            # convert integer to str: to find pali
            num = str(i)
            # check pali
            if (num == num[::-1]):
                # check prime
                if (isPrime(i) == 1):
                    yield 'PaliPrimes',int(i)
# end mapfn
# start reducefn
def reducefn(k, vs):
    # meh => total sum: to test if correct (will be 1 off(compared to given example) not using 0 or 1 as prime)
    meh = sum(vs)
    # lon => total length: how many values were found (will be 2 off(compared to given example) not using 0 or 1 as prime)
    lon = len(vs)
    return vs,meh,lon
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
