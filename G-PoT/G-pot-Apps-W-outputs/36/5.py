
n = int(input())
array = list(map(int, input().split()))

array_set = set(array)
max_freq = max(array.count(num) for num in array)

if max_freq <= (n + 1) // 2:
    print("YES")
else:
    print("NO")
