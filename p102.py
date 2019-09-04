
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return "("+str(self.x)+", "+str(self.y)+")"

class Triangle:
    def __init__(self, p1=Point(), p2=Point(), p3=Point()):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        
    def contains(self, p):
        t = line(self.p1, self.p2)
        u = line(self.p2, self.p3)
        v = line(self.p3, self.p1)
        if sign(t[0]*self.p3.x+t[1]*self.p3.y+t[2])!=sign(t[0]*p.x+t[1]*p.y+t[2]):
            return False
        if sign(u[0]*self.p1.x+u[1]*self.p1.y+u[2])!=sign(u[0]*p.x+u[1]*p.y+u[2]):
            return False
        if sign(v[0]*self.p2.x+v[1]*self.p2.y+v[2])!=sign(v[0]*p.x+v[1]*p.y+v[2]):
            return False
        return True
        

def line(p1, p2):
    '''
    y = (y2-y1)/(x2-x1)x + b
    y(x2-x1) = x(y2-y1) + b(x2-x1)
    a = y2-y1
    b = x1-x2
    c = (y1(x2-x1) - x1(y2-y1))
    = y1x2 - x1y2
    '''
    a = p2.y - p1.y
    b = p1.x - p2.x
    c = p1.y*p2.x - p1.x*p2.y
    return a,b,c

def sign(a):
    return (a > 0) - (a < 0)

n = 0
with open('p102_triangles.txt', 'r') as f:
    for coordline in f:
        pts = list(map(int, coordline.split(',')))
        a = Point(pts[0], pts[1])
        b = Point(pts[2], pts[3])
        c = Point(pts[4], pts[5])
        t = Triangle(a, b, c)
        if t.contains(Point()):
            n += 1

print(n)

f.close()

