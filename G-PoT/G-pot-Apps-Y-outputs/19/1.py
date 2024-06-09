
n = int(input())
a = list(map(int, input().split()))

increasing = []
decreasing = []

prev = a[0]
increasing.append(prev)
increasing_flag = True

for i in range(1, n):
    if a[i] > prev:
        if increasing_flag:
            increasing.append(a[i])
        else:
            print("NO")
            break
    elif a[i] < prev:
        increasing_flag = False
        decreasing.append(a[i])
    else:
        print("NO")
        break
    prev = a[i]
else:
    print("YES")
    print(len(increasing))
    print(*increasing)
    print(len(decreasing))
    print(*decreasing[::-1])
