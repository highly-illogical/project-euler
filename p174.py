
def laminae(n):
    tiles = [0 for i in range(n)]
    side = 3
    t = 0
    while (side**2 - (side-2)**2) <= n:
        hole = side-2
        while hole > 0:
            ntiles = side**2 - hole**2
            if ntiles <= n:
                t += 1
                hole -= 2
                tiles[ntiles-1] += 1
            else:
                break
        side += 1
    return tiles

a = laminae(10**6)
print(sum(a.count(i) for i in range(1,11)))

