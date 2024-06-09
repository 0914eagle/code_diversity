
n = int(input())
a = list(map(int, input().split()))

increasing = []
decreasing = []

last = -1
for num in a:
    if num > last:
        increasing.append(num)
        last = num
    elif num < last:
        decreasing.append(num)
        last = num
    else:
        print("NO")
        break
else:
    print("YES")
    print(len(increasing))
    print(*increasing)
    print(len(decreasing))
    print(*decreasing[::-1])
