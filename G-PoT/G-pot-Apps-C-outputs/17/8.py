
n, m = map(int, input().split())
candies = []
for _ in range(m):
    a, b = map(int, input().split())
    candies.append((a, b))

def calculate_time(start):
    time = 0
    for a, b in candies:
        if a <= start:
            time += min(b - a, n - start + b)
        else:
            time += a - start + b
    return time

result = []
for i in range(1, n+1):
    result.append(calculate_time(i))

print(*result)
