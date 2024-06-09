
x = []
r, D, x_2000 = map(int, input().split())

for i in range(2000, 2011):
    x.append(int(r * x[-1] - D))

for i in x:
    print(i)

