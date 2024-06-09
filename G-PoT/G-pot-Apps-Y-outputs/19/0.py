
n = int(input())
a = list(map(int, input().split()))

increasing = []
decreasing = []

for num in a:
    if not increasing or num > increasing[-1]:
        increasing.append(num)
    elif not decreasing or num < decreasing[-1]:
        decreasing.append(num)
    else:
        print("NO")
        break
else:
    print("YES")
    print(len(increasing))
    print(*increasing)
    print(len(decreasing))
    print(*decreasing[::-1])
