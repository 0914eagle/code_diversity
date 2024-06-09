
r, D, x_2000 = map(int, input().split())

x_list = []
for i in range(2000, 2011):
    x = r * x_list[-1] - D if i > 2000 else x_2000
    x_list.append(x)

for x in x_list:
    print(x)

