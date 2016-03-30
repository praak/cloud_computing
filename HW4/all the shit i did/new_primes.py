#!/usr/bin/env python
import mincemeat
import sys
# import line_profiler

data = list(range(1000000))
datasource = dict(enumerate(data))

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

    if (v is 2):
        yield 'PaliPrimes',int(v)

    if ((v % 2) is not 0) or ((v % 3) is not 0) or ((v % 5) is not 0) or ((v % 7) is not 0):
        num = str(v)
        if (num == num[::-1]):
            if (isPrime(v) == 1):
                yield 'PaliPrimes',int(v)

def reducefn(k, vs):
    meh = sum(vs)
    lon = len(vs)
    return lon,meh,vs

s = mincemeat.Server()
s.datasource = datasource
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")
lon , meh , vs = results['PaliPrimes']

print('Palindromes:' , vs)
print('Sum :' , meh)
print('Length:' , lon)

