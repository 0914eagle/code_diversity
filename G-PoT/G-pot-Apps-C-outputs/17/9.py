
n, m = map(int, input().split())
candies = []
for _ in range(m):
    a, b = map(int, input().split())
    candies.append((a, b))

def calculate_time(start):
    time = 0
    for a, b in candies:
        time += min(abs(a - start) + abs(b - a), n - abs(a - start) + abs(b - a))
    return time

for i in range(1, n+1):
    print(calculate_time(i), end=' ')
