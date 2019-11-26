
maxsum = 0
terms = [a**b for a in range(1,100) for b in range(1,100)]
for t in terms:
    maxsum = max(maxsum, sum(int(i) for i in str(t)))
print(maxsum)

