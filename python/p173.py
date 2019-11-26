
def laminae(n):
    side = 3
    t = 0
    while (side**2 - (side-2)**2) <= n:
        hole = side-2
        while hole > 0:
            if side**2 - hole**2 <= n:
                t += 1
                hole -= 2
            else:
                break
        side += 1
    return t

print(laminae(10**6))

