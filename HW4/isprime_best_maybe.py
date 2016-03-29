#!/usr/bin/env python
import mincemeat
import sys
# import line_profiler

data = list(range(1000000))
datasource = dict(enumerate(data))

def mapfn(k, v):
    import math
# // leastFactor(n)
# // returns the smallest prime that divides n
# //     NaN if n is NaN or Infinity
# //      0  if n=0
# //      1  if n=1, n=-1, or n is not an integer

    def leastFactor(n):
        if (n == 0):
            return 0
        if (n%1):
            return 1
        if ((n%2)==0):
            return 2
        if ((n%3)==0):
            return 3
        if ((n%5)==0):
            return 5
        m = int(math.sqrt(n));
        for i in range(7,m+1,30):
            if (n%i==0):
                return i
            if (n%(i+4)==0):
                return i+4
            if (n%(i+6)==0):
                return i+6
            if (n%(i+10)==0):
                return i+10
            if (n%(i+12)==0):
                return i+12
            if (n%(i+16)==0):
                return i+16
            if (n%(i+22)==0):
                return i+22
            if (n%(i+24)==0):
                return i+24
        return n;

    # def isPrime(v):
    #     flag = 1
    #     # print v,'isPrime'
    #     for i in (range(2,((int(math.ceil(math.sqrt(v))))+1))):
    #         if ((v % i) is 0):
    #             flag = 0
    #             break
    #     # print flag,'after prime check'
    #     return flag
    def isPrime(v):
        if (v % 1) or (v<2):
            return False;
        if (v == leastFactor(v)):
            return True;
        return False;

    # if ((v % 2) is not 0) or ((v % 3) is not 0) or ((v % 5) is not 0) or ((v % 7) is not 0):
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
