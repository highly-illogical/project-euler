
primes = {1:2, 2:3, 3:5, 4:7, 5:11, 6:13, 7:17, 8:19, 9:23, 10:29, 11:31, 12:37,
          13:41, 14:43, 15:47, 16:53, 17:59, 18:61, 19:67, 20:71, 21:73, 22:79,
          23:83, 24:89, 25:97}

def primesums(p, i):
    if p <= 1 or i <= 0:
        return 0
    elif i == 1:
        return 0 if p%primes[i] else 1
    elif p < primes[i]:
        return primesums(p, i-1)
    else:
        s = primesums(p, i-1)
        s += sum(primesums(p-j, i-1) for j in range(primes[i], p+1, primes[i]))
        if p%primes[i]==0:
            s += 1
        return s
		
for i in range(1,100):
	print(i, primesums(i,25))

