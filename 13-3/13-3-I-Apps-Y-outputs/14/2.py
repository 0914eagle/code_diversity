
r, D, x_2000 = map(int, input().split())

for i in range(2001, 2011):
    x_i = r * x_i - D
    print(x_i)

