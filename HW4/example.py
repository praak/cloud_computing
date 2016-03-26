#!/usr/bin/env python
import mincemeat
import sys
# data = ["Humpty Dumpty sat on a wall",
#         "Humpty Dumpty had a great fall",
#         "All the King's horses and all the King's men",
#         "Couldn't put Humpty together again",
#         ]

# file = open('numbers.txt')
file = open(sys.argv[-1],'r')

# The data source can be any dictionary-like object
# datasource = dict(enumerate(data))

data = list(file)
file.close()

# datasource = dict(enumerate(data))
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

    print ("Average: %f" % average)
    print ("Count: %d" % len(vs))
    print ("Standard Deviation: %f" % std_dv)
    print ("Sum: %f" % total)

    return len(vs), total, std_dv, average
    # print("reducing shit...")
    # for v in vs:
    #     print(v)
    # result = sum(vs)
    # return result

s = mincemeat.Server()
s.datasource = datasource
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")
count, total, std_dv, average = results['Value']
print("Count: %d \nSum: %f \nStandard Deviation: %f \nMean: %f" % (count,total,std_dv,average))
