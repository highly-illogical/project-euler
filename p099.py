
from math import log

f = open('p099_base_exp.txt','r')
mval = 0
mnum = -1
i = 0
for line in f:
    i += 1
    be = line.split(',')
    b,e = int(be[0]),int(be[1])
    logval = e*log(b)
    if logval > mval:
        mval = logval
        mnum = i

print(mnum)
        
f.close()

