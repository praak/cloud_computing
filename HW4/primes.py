#!/usr/bin/env python
import mincemeat
import sys

# file = open(sys.argv[-1],'r')
data = list(range(10000))
# file.close()
datasource = dict(enumerate(data))
# print("Data:")
# print(datasource)
print("Return...")

def mapfn(k, v):
    import math
    # for n in range(1,20):
    # not needed for n range, as thats our data incoming.
    if (v is 2) or (v is 3):
        yield 'Primes',int(v)
    elif ((v % 2) is 0) or ((v % 3) is 0):
        return
    else:
        # n = int(v)
        flag = 1
        for i in (range(5,int(math.ceil(math.sqrt(v))))):
            if ((v % i) is 0):
                flag = 0
                break
            #endif
        #endfor i
        if flag == 1:
            print("Prime:")
            print(v)
            yield 'Primes',int(v)
    #end else n
#endmapfn

def reducefn(k, vs):
    # print(vs)
    pali = vs[:]
    for v in vs:
        if (v == 0) or (v == 1):
            pali.remove(v)
        num = str(v)
        for ind in range(0,((len(num)/2)+1)):
            last = num[(len(num)-1)-ind]
            first =  num[ind]
            if last is not first:
                pali.remove(v)
                break

    return pali

s = mincemeat.Server()
s.datasource = datasource
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")
print results
