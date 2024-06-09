
n = int(input())
a = list(map(int, input().split()))

increasing = []
decreasing = []

i = 0
while i < n and (i == 0 or a[i] > a[i-1]):
    increasing.append(a[i])
    i += 1

while i < n and (i == 1 or a[i] < a[i-1]):
    decreasing.append(a[i])
    i += 1

if len(increasing) + len(decreasing) == n:
    print("YES")
    print(len(increasing))
    print(*increasing)
    print(len(decreasing))
    print(*decreasing)
else:
    print("NO")
