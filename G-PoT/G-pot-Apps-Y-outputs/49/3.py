
n = int(input())
a = list(map(int, input().split()))

def check_increasing(arr):
    for i in range(len(arr) - 1):
        if arr[i] >= arr[i+1]:
            return False
    return True

max_len = 1
for i in range(n):
    if i > 0 and i < n-1 and a[i-1] < a[i+1]:
        max_len = max(max_len, i+1)
        continue
    subarray = a[:i] + a[i+1:]
    if check_increasing(subarray):
        max_len = max(max_len, len(subarray))

print(max_len)
