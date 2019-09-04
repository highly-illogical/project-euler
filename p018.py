
t = []
with open('p018.txt', 'r') as f:
    for line in f:
        l = line.split(' ')
        t.append([int(i) for i in l])

f.close()

for i in range(len(t)-1):
    for j in range(len(t[-2-i])):
        t[-2-i][j] += max(t[-1-i][j], t[-1-i][j+1])

print(t[0])

