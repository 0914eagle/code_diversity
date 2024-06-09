
n = int(input())
array = list(map(int, input().split()))

array.sort()

for i in range(n - 1):
    if array[i] == array[i + 1]:
        print("YES")
        break
else:
    print("NO")
