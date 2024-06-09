
n = int(input())
a = []
for i in range(n):
    a.append(float(input()))

b = []
for i in range(n):
    if a[i] >= 0:
        b.append(int(a[i] + 0.5))
    else:
        b.append(int(a[i] - 0.5))

for i in range(n):
    print(b[i])

