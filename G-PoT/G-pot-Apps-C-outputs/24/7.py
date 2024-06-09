
n = int(input())

max_beauty = n
for i in range(n):
    max_beauty ^= i

print(max_beauty)
permutation = []
for i in range(n+1):
    permutation.append(max_beauty ^ i)

print(*permutation)
