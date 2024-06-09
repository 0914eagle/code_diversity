
n, m = map(int, input().split())
candies = []
for _ in range(m):
    a, b = map(int, input().split())
    candies.append((a, b))

def time_to_deliver(candies, start):
    time = 0
    for a, b in candies:
        time += min(abs(a - start), n - abs(a - start)) + min(abs(b - a), n - abs(b - a))
    return time

for i in range(1, n+1):
    print(time_to_deliver(candies, i), end=' ')
