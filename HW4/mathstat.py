#!/usr/bin/env python
import mincemeat
import sys

file = open(sys.argv[-1],'r')
something = list(file)

data = []
lit = []
siz = len(something)/60 + 2

for i in something:
    lit.append(i)
    if len(lit)==siz:
        data.append(lit)
        lit = []

data.append(lit)
file.close()

datasource = dict(enumerate(data))

def mapfn(k, v):
    count = 0.0
    total = 0.0
    squares = 0.0
    # throwing list into one string
    v = ''.join(v)
    for w in v.split():
        total += float(w)
        squares += float(w)**2
        count += 1
    yield 'Value', (total,squares,count)

def reducefn(k, vs):
    import math

    stotal = 0.0
    ssquares = 0.0
    scount = 0.0
    for i in vs:
        (total,squares,count) = i
        stotal += total
        ssquares += squares
        scount += count

    std_dv = math.sqrt((1/(scount-1))*(ssquares - ((1/scount)*(stotal**2))))
    return (std_dv,scount,stotal)

s = mincemeat.Server()
s.datasource = datasource
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")
(std_dv, count, total) = results['Value']
print("Count: %d \nSum: %f \nStandard Deviation: %f" % (count,total,std_dv))
