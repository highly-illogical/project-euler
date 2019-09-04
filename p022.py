
f = open('p022_names.txt','r')

t = 0
for line in f:
    w = sorted(line.split(','))
    for i in range(len(w)):
        name = w[i][1:-1]
        sn = 0
        for c in name:
            sn += ord(c)-64
        t += sn*(i+1)
        
print(t)
f.close()

