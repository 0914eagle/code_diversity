
n = int(input())
arr = list(map(int, input().split()))

count = 0
while arr:
    count += 1
    curr = arr[0]
    for i in range(1, len(arr)):
        if arr[i] != curr:
            break
    arr = arr[i:]

print(count)

