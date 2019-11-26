
def digits(n): return sorted(list(str(n)))

def same(n):
    k = digits(n)
    for i in range(2,7):
        if digits(i*n)!= k:
            return False
    return True

f = False
i = 0
while not f:
    i += 1
    if same(i):
        f = True
        print(i)
		
