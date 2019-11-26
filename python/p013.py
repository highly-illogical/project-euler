
f = open('e013.txt','r')
s = 0
for line in f:
    s += int(line)
f.close()
print(str(s)[:10])

