
def ispalin(n):
    s = str(n)
    for i in range(len(s)):
        if s[i]!=s[-i-1]:
            return False
    return True
    
palins = [n1*n2 for n1 in range(100,1000) for n2 in range(100,1000) \
          if ispalin(n1*n2)]

print(max(palins))

