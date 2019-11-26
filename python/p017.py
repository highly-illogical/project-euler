
counts = {1:3, 2:3, 3:5, 4:4, 5:4, 6:3, 7:5, 8:5, 9:4, 10:3,
          11:6, 12:6, 13:8, 14:8, 15:7, 16:7, 17:9, 18:8, 19:8, 20:6,
          30:6, 40:5, 50:5, 60:5, 70:7, 80:6, 90:6}

def count(n):
    if n==1000:
        return 11
    else:
        hundreds = counts[n//100]+10 if n>99 else 0
        rest = n%100
        if rest==0:
            return hundreds-3
        elif rest<20:
            return hundreds+counts[rest]
        else:
            tens = counts[10*(rest//10)]
            units = counts[rest%10] if rest%10 else 0
            return hundreds+tens+units

print(sum([count(i) for i in range(1,1001)]))

