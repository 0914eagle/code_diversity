
x, y = map(int, input().split())

count = 0
while x != y:
    if x > y:
        x = (x + 2) // 3
    else:
        x = (x + 1) // 3
    count += 1

print(count)
