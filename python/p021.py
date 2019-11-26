
def divisorsum(n):
    s = 0
    for k in range(1,n):
        if not n%k: s += k
    return s

def amicable(n):
    d = divisorsum(n)
    if d!=n and divisorsum(d)==n:
        return True
    return False
    
print(sum(i for i in range(2,10000) if amicable(i)))

