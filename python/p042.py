
f = open('p042_words.txt', 'r')

def triangle(n): return n*(n+1)//2

triangles = [triangle(i) for i in range(1,1000)]

nt=0
for line in f:
    w = line.split(',')
    for k in w:
        word = k[1:-1]
        sw = 0
        for c in word:
            sw += ord(c)-64
        if sw in triangles:
            nt += 1

print(nt)

f.close()

