
n = int(input())
durabilities = list(map(int, input().split()))

total_shots = sum(d * (n-1) + 1 for d in durabilities)
order = list(range(1, n+1))

print(total_shots)
print(' '.join(map(str, order)))
