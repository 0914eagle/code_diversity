
n, m = map(int, input().split())
buttons = list(map(int, input().split()))

lights = [0] * (n + 1)

for button in buttons:
    lights[button] = button

for i in range(n, 0, -1):
    if lights[i] == 0:
        lights[i] = lights[i + 1]

print(*lights)

