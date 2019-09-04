
def triangle(n): return n*(n+1)//2
def pentagon(n): return n*(3*n-1)//2
def hexagon(n): return n*(2*n-1)

f = 0
t,p,h = 1,1,1
while f<2:
    t+=1
    while pentagon(p)<=triangle(t): p+=1
    p-=1
    while hexagon(h)<=triangle(t): h+=1
    h-=1
    if triangle(t)==pentagon(p) and triangle(t)==hexagon(h):
        f+=1
        print(t, triangle(t))
		
