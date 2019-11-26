
terms = [a**b for a in range(2,101) for b in range(2,101)]
unique = []
for t in terms:
    if t not in unique:
        unique.append(t)

print(len(unique))

