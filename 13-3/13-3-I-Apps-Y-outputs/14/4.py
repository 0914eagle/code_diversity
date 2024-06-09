
r, D, x_2000 = map(int, input().split())

x_list = [x_2000]

for i in range(10):
    x_list.append(int(r * x_list[i] - D))

for x in x_list[1:]:
    print(x)

