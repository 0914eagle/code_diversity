
n = int(input())

max_beauty = n
for i in range(n):
    max_beauty ^= i

print(max_beauty)
perm = [i for i in range(n+1)]
print(*perm)
