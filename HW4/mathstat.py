#!/usr/bin/env python
import mincemeat
import sys

file = open(sys.argv[-1],'r')
data = list(file)
file.close()
datasource = dict(enumerate(data))

def mapfn(k, v):
    for w in v.split():
        yield 'Value', float(w)

def reducefn(k, vs):
    import math

    total, std_dv, average = 0.0, 0.0, 0.0
    total = sum(vs)
    average = total/len(vs)
    for i in range(0, len(vs)):
        std_dv = std_dv + ((vs[i] - average)**2)
    std_dv = math.sqrt(std_dv/len(vs))

    print ("Average: %f \nCount: %d \nStandard Deviation: %f \nSum: %d" % (average,len(vs),std_dv,total))

    return len(vs), total, std_dv, average

s = mincemeat.Server()
s.datasource = datasource
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")
count, total, std_dv, average = results['Value']

print("Count: %d \nSum: %f \nStandard Deviation: %f \nMean: %f" % (count,total,std_dv,average))
