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

    flag = 0
    if (v is 1) or (v is 2) or (v is 3) or (v is 5) or (v is 7):
        yield 'PaliPrimes',int(v)
    elif ((v % 2) is not 0) or ((v % 3) is not 0) or ((v % 5) is not 0) or ((v % 7) is not 0):
        num = str(v)
        for ind in range(0,((len(num)/2)+1)):
            last = num[(len(num)-1)-ind]
            first =  num[ind]
            if last is not first:
                flag = 0
                return
            else:
                flag = 1
    else:
        return

    if (flag == 1):
        if (isPrime(v) == 1):
            yield 'PaliPrimes',int(v)

    return

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

