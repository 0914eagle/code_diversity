
n = int(input())
durabilities = list(map(int, input().split()))

total_shots = 0
order = []

for i in range(n):
    total_shots += (i * durabilities[i] + 1)
    order.append(i+1)

print(total_shots)
print(' '.join(map(str, order)))
