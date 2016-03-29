#!/usr/bin/env python
import mincemeat
import sys
# import line_profiler

# file = open(sys.argv[-1],'r')
data = list(range(50))
# file.close()
datasource = dict(enumerate(data))


def mapfn(k, v):
    knownprimes = [2,3]
    # for n in range(1,20):
    # not needed for n range, as thats our data incoming.
    if (v is 2) or (v is 3):
        yield v,1
    elif ((v % 2) is 0) or ((v % 3) is 0) or (v == 1):
        return
    else:
        # n = int(v)
        flag = 1
        for i in knownprimes:
            if ((v % i) is 0):
                flag = 0
                break
            #endif
        #endfor i
        if flag == 1:
            knownprimes.append(v)
            yield v,1


def reducefn(k, vs):
    print(k,vs)
    print('..')
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


