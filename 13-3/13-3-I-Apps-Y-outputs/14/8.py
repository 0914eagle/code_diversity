
r, D, x_2000 = map(int, input().split())

x_list = []
x_list.append(x_2000)

for i in range(10):
    x_list.append(int(r * x_list[i] - D))

for i in range(10):
    print(x_list[i+1])

