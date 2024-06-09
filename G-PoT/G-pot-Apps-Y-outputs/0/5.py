
n = int(input())
durabilities = list(map(int, input().split()))

total_shots = 0
order = []

for i in range(n):
    total_shots += durabilities[i] * (n - 1) + 1
    order.append(i+1)

print(total_shots)
print(*order)
