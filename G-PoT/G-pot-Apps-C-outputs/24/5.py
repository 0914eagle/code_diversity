
n = int(input())

if n % 4 == 0:
    beauty = n
elif n % 4 == 1:
    beauty = 1
elif n % 4 == 2:
    beauty = n + 1
else:
    beauty = 0

permutation = []
for i in range(n):
    if i % 4 == 0 or i % 4 == 1:
        permutation.append(i)
    else:
        permutation.insert(0, i)

print(beauty)
print(' '.join(map(str, permutation)))
