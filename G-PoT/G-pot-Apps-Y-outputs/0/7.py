
n = int(input())
durabilities = list(map(int, input().split()))

shots = 0
order = list(range(1, n+1))

for i in range(n):
    shots += durabilities[i] * (n-i) + 1

print(shots)
print(' '.join(map(str, order)))
