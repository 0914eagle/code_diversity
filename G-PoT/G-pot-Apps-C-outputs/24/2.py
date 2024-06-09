
n = int(input())

beauty = n
for i in range(n):
    beauty ^= i

print(beauty)
print(*range(n+1))
