
n, m = map(int, input().split())
buttons = list(map(int, input().split()))

lights = [1] * n

for button in buttons:
    for i in range(button, n):
        if lights[i] == 1:
            lights[i] = button

print(*lights)

