
n, m = map(int, input().split())
s = input()

for i in range(m):
    x, y = input().split()
    s = s.replace(x, y).replace(y, x)

print(s)

