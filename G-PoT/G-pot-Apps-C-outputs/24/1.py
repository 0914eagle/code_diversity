
n = int(input())

max_beauty = n
for i in range(n):
    max_beauty ^= i

print(max_beauty)
print(*range(n+1))
