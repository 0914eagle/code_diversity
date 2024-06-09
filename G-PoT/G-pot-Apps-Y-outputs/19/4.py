
n = int(input())
a = list(map(int, input().split()))

increasing = []
decreasing = []

i = 0
while i < n - 1 and a[i] < a[i + 1]:
    increasing.append(a[i])
    i += 1

while i < n - 1 and a[i] > a[i + 1]:
    decreasing.append(a[i])
    i += 1

if i < n - 1:
    print("NO")
else:
    if a[n - 1] > increasing[-1]:
        increasing.append(a[n - 1])
    else:
        decreasing.append(a[n - 1])

    print("YES")
    print(len(increasing))
    print(*increasing)
    print(len(decreasing))
    print(*decreasing[::-1])
