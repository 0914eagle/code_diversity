
n, m = map(int, input().split())
field = [input() for _ in range(n)]

# Check if the field is rectangular
if len(set(map(len, field))) != 1:
    print("NO")
    exit()

# Check if the field has three colors
colors = set()
for row in field:
    for col in row:
        colors.add(col)
if len(colors) != 3:
    print("NO")
    exit()

# Check if the field has three equal width and height stripes
if n % 3 != 0 or m % 3 != 0:
    print("NO")
    exit()

# Check if each color is used in exactly one stripe
for i in range(0, n, 3):
    for j in range(0, m, 3):
        color = field[i][j]
        for k in range(i, i+3):
            for l in range(j, j+3):
                if field[k][l] != color:
                    print("NO")
                    exit()

print("YES")

