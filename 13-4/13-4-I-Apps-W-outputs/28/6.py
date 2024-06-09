
n, m = map(int, input().split())
buttons = list(map(int, input().split()))

lights_off = [0] * n
for button in buttons:
    for i in range(button, n):
        if lights_off[i] == 0:
            lights_off[i] = button

print(*lights_off)

