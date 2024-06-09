
n, m = map(int, input().split())
buttons = list(map(int, input().split()))

lights = [0] * (n + 1)
for i in range(m):
    button = buttons[i]
    for j in range(button, n + 1):
        if lights[j] == 0:
            lights[j] = button

print(*lights[1:], sep=' ')

