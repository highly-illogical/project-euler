
def sieve(n):
    i = 1
    primes = []
    while not len(primes) or primes[-1]<n:
        i += 1
        prime = True
        for p in primes:
            if i%p==0:
                prime = False
                break
        if prime: primes.append(i)
    return primes

primes = sieve(7072)

second, third, fourth = 0,0,0
a = 0
lim = 5*10**7
i,j,k = 0,0,0
nums = []

while i<len(primes):
    fourth, third, second = primes[i], primes[j], primes[k]
    a = fourth**4+third**3+second**2
    if a < lim:
        nums.append(a)
        k += 1
    elif k > 1:
        k = 0
        j += 1
    else:
        k = 0
        j = 0
        i += 1

print(len(nums))

nums.sort()

n = 1 + sum(1 for i in range(1,len(nums)) if nums[i]!=nums[i-1])

print(n)

