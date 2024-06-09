
n = int(input())
durabilities = list(map(int, input().split()))

shots = 0
order = []

for i in range(n):
    shots += (i * durabilities[i] + 1)
    order.append(i+1)

print(shots)
print(*order)
