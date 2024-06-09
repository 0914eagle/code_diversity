
n = int(input())
arr = list(map(int, input().split()))

count = 0
while arr:
    count += 1
    temp = []
    for i in range(1, len(arr)):
        if arr[i] == arr[i-1]:
            temp.append(arr[i])
    arr = [arr[0]] + temp

print(count)

