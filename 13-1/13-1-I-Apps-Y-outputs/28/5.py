
n, k = map(int, input().split())
arr = list(map(int, input().split()))

left = 0
right = n - 1
count = 0

while left <= right:
    if arr[left] <= k:
        count += 1
        left += 1
    if arr[right] <= k:
        count += 1
        right -= 1
    if left <= right:
        count += 1
        left += 1
        right -= 1

print(count)

