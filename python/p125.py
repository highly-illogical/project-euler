
import math

palins = filter(lambda i: str(i)==str(i)[::-1], range(1,10**8))
    
sqsums = [i*(i+1)*(2*i+1)//6 for i in range(2*10**4+10)]

def issum(n):
    for i in range(2, int(math.sqrt(n))+1):
        mid = int(math.e**(math.log(n/i)/2))
        minim = mid-i if mid-i > 1 else 1
        maxim = mid+i if mid+i < len(sqsums) else len(sqsums)
        sqs = sqsums[minim+i-1]-sqsums[minim-1]
        for j in range(minim+i, maxim+2):
            if sqs==n:
                print(n)
                return True
            sqs = sqsums[j]-sqsums[j-i]
    return False

s = 0

for p in palins:
    if issum(p):
        s += p

def sqdiff(a,b):
    return (a*(a+1)*(2*a+1)-b*(b+1)*(2*b+1))/6

print(s)

