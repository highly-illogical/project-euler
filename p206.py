
for m in range(0,5*10**7,10):
    i = 10**8+m+3
    sq = str(i**2)
    if sq[::2]=='123456789':
        print(sq)
    i = 10**8+m+7
    sq = str(i**2)
    if sq[::2]=='123456789':
        print(sq, i)
		
