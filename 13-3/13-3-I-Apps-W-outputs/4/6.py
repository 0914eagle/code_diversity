
n, k = map(int, input().split())
a = list(map(int, input().split()))

days = 0
candies = 0

for i in range(n):
    candies += a[i]
    days += 1
    if candies >= k:
        break
    if days == n and candies < k:
        print(-1)
        break
    if candies >= 8:
        candies -= 8
        days += 1
        if candies >= k:
            break

print(days)

