
n = int(input())
durabilities = list(map(int, input().split()))

total_shots = sum(durabilities) + n - max(durabilities)

order = sorted(range(1, n+1), key=lambda x: durabilities[x-1], reverse=True)

print(total_shots)
print(' '.join(map(str, order)))
