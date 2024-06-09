
n, m = map(int, input().split())
field = [input() for _ in range(n)]

# Check if the field is rectangular
if len(set(map(len, field))) != 1:
    print("NO")
    exit()

# Check if the field has three colors
colors = set()
for row in field:
    for color in row:
        colors.add(color)
if len(colors) != 3:
    print("NO")
    exit()

# Check if the field has three equal-width stripes
width = len(field[0]) // 3
if width * 3 != len(field[0]):
    print("NO")
    exit()

# Check if the field has three equal-height stripes
height = len(field) // 3
if height * 3 != len(field):
    print("NO")
    exit()

# Check if the colors are used only once in each stripe
for i in range(3):
    for j in range(3):
        color = field[i * height][j * width]
        for row in field[i * height:(i + 1) * height]:
            if color in row[j * width:(j + 1) * width]:
                if row[j * width:(j + 1) * width].count(color) > 1:
                    print("NO")
                    exit()

print("YES")

