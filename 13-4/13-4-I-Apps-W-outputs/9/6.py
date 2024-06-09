
n, m = map(int, input().split())
name = input()

for i in range(m):
    x, y = input().split()
    name = name.replace(x, y).replace(y, x)

print(name)

