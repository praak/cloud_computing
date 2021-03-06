#!/usr/bin/env python
import mincemeat
import sys
# import line_profiler

# file = open(sys.argv[-1],'r')
data = list(range(20))
# file.close()
datasource = dict(enumerate(data))
# print("Data:")
# print(datasource)
# @profile
def mapfn(k, v):
    import math
    def ispali(v):
        if (v != 0) or (v != 1):
            num = str(v)
            flag = 0
            for ind in range(0,((len(num)/2)+1)):
                    last = num[(len(num)-1)-ind]
                    first =  num[ind]
                    if last is not first:
                        flag = 0
                        break
                    else:
                        flag = 1
        return flag
    # for n in range(1,20):
    # not needed for n range, as thats our data incoming.
    if (v is 2) or (v is 3):
        yield 'PaliPrimes',int(v)
    elif ((v % 2) is 0) or ((v % 3) is 0):
        return
    else:
        # n = int(v)
        flag = 1
        for i in (range(5,int(math.ceil(math.sqrt(v))))):
        # for i in (range(5,((int((v)**(0.5))))+2)):
            if ((v % i) is 0):
                flag = 0
                break
            #endif
        #endfor i
        if flag == 1:
            # print("Prime:")
            # print(v)
            if ispali(v):
                yield 'PaliPrimes',int(v)
    #end else n
#endmapfn

def reducefn(k, vs):
    lon = len(vs)
    meh = sum(vs)
    return meh,vs,lon

s = mincemeat.Server()
s.datasource = datasource
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")
lon , meh , vs = results['PaliPrimes']

print('Palindromes:' , vs)
print('Sum : %d' % meh)
print('Length: %d' % lon)

