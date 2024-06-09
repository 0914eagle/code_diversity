
n = int(input())
arr = list(map(int, input().split()))

count = 0
while arr:
    count += 1
    temp = arr[0]
    arr = [x for x in arr if x != temp]

print(count)

