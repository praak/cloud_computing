# Praakrit Pradhan
# Computer Engineering
# Cloud Computing
# Universtiy of Cincinnati
#!/usr/bin/env python
# Problem Statement: find Standard Deviation, Total and Count of data given to your map/reduce in one run through the data.
import mincemeat
import sys

# take the file path from command line
# [-1] takes the last string array inputted
file = open(sys.argv[-1],'r')
# throws it into a list
something = list(file)
# empty lists for grouping the big file
data = []
lit = []
# size for grouping. 60 just an arbitrary group size
siz = len(something)/60 + 2
# grouping up the list into tuples
for i in something:
    lit.append(i)
    if len(lit)==siz:
        data.append(lit)
        lit = []
# appending last set of data (if this isnt done the last bit isnt added)
data.append(lit)
file.close()

datasource = dict(enumerate(data))

# start mapfn
def mapfn(k, v):
    # initialize variables
    count = 0.0
    total = 0.0
    squares = 0.0
    # throwing list into one string
    v = ''.join(v)
    for w in v.split():
        total += float(w)
        squares += float(w)**2
        count += 1
    # passing back a tuple of the total/squares/count
    yield 'Value', (total,squares,count)
# end mapfn
# start reducefn
def reducefn(k, vs):
    import math
    # initializing the counter for sum of total/squares/count
    stotal = 0.0
    ssquares = 0.0
    scount = 0.0
    # starting loop to traverse vs
    for i in vs:
        # taking out the total/square/count
        (total,squares,count) = i
        # summing them up
        stotal += total
        ssquares += squares
        scount += count
    # finding the standard deviation w/o average -> diff formulae
    std_dv = math.sqrt((1/(scount-1))*(ssquares - ((1/scount)*(stotal**2))))
    return (std_dv,scount,stotal)
# end reducefn

# server setup stuff for map/reduce
s = mincemeat.Server()
s.datasource = datasource
s.mapfn = mapfn
s.reducefn = reducefn
# pulling out all results
results = s.run_server(password="changeme")
(std_dv, count, total) = results['Value']
# printing the final results
print("Count: %d \nSum: %f \nStandard Deviation: %f" % (count,total,std_dv))
