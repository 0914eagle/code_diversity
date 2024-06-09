
n, m = map(int, input().split())
buttons = list(map(int, input().split()))

result = [-1] * (n + 1)

for i in range(m):
    button = buttons[i]
    for j in range(button, n + 1):
        if result[j] == -1:
            result[j] = i + 1
            break

print(*result[1:])

