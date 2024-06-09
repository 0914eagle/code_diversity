
n, k = map(int, input().split())
skills = list(map(int, input().split()))

left = 0
right = n - 1
count = 0

while left <= right:
    if skills[left] <= k:
        count += 1
        left += 1
    if skills[right] <= k:
        count += 1
        right -= 1
    if left <= right:
        count += 1
        left += 1
        right -= 1

print(count)

