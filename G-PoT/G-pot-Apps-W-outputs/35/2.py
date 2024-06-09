
a, b, c = map(int, input().split())

sides = [a, b, c]
sides.sort()

if sides[0] + sides[1] > sides[2]:
    print(0)
else:
    print(sides[2] - sides[1] - sides[0] + 1)
