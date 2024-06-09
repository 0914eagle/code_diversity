
n = int(input())
arr = list(map(int, input().split()))

arr_set = set(arr)
max_freq = max(arr.count(x) for x in arr)

if max_freq <= (n + 1) // 2:
    print("YES")
else:
    print("NO")
