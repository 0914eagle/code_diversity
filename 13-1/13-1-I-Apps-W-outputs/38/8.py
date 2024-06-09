
n = int(input())
a = list(map(int, input().split()))

x_count = 0
for i in range(1, 100001):
    if a.count(i) > 1:
        x_count += 1
        print(i, a.count(i) - 1)
    elif a.count(i) == 1:
        x_count += 1
        print(i, 0)

print(x_count)

