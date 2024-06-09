
n, m = map(int, input().split())
candies = []
for _ in range(m):
    a, b = map(int, input().split())
    candies.append((a, b))

def min_time_to_deliver(n, m, candies, start):
    time = 0
    for i in range(m):
        time += min((candies[i][1] - candies[i][0] + n) % n, (candies[i][0] - candies[i][1] + n) % n) + 1
    return time

result = []
for i in range(1, n+1):
    result.append(min_time_to_deliver(n, m, candies, i))

print(*result)
