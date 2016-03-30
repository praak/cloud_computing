#!/usr/bin/env python
import mincemeat
import sys
# import line_profiler

# file = open(sys.argv[-1],'r')
# siz = 10000
siz = 10000000/60 + 2
data = []
lit = []

for i in range(1,10000000):
    lit.append(i)
    if len(lit)==siz:
        data.append(lit)
        lit = []

data.append(lit)

datasource = dict(enumerate(data))
# print data

def mapfn(k, v):
    import math
    def isPrime(v):
        flag = 1
        # print v,'isPrime'
        for i in (range(2,((int(math.ceil(math.sqrt(v))))+1))):
            if ((v % i) is 0):
                flag = 0
                break
        # print flag,'after prime check'
        return flag

    for i in v:
        if (i is 2):
            yield 'PaliPrimes',int(i)

        if ((i % 2) is not 0) or ((i % 3) is not 0) or ((i % 5) is not 0) or ((i % 7) is not 0):
            num = str(i)
            if (num == num[::-1]):
                if (isPrime(i) == 1):
                    yield 'PaliPrimes',int(i)

def reducefn(k, vs):
    meh = sum(vs)
    lon = len(vs)
    return vs,meh,lon


s = mincemeat.Server()
s.datasource = datasource
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")
print results
