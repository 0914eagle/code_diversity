
n = int(input())
a = list(map(int, input().split()))

increasing = []
decreasing = []

prev = a[0]
increasing.append(prev)
is_increasing = True

for i in range(1, n):
    if a[i] > prev:
        if is_increasing:
            increasing.append(a[i])
        else:
            is_increasing = False
            break
    elif a[i] < prev:
        if not is_increasing:
            decreasing.append(a[i])
        else:
            is_increasing = False
            break
    else:
        is_increasing = False
        break
    prev = a[i]

if is_increasing:
    print("YES")
    print(len(increasing))
    print(*increasing)
    print(len(decreasing))
    print(*decreasing[::-1])
else:
    print("NO")
