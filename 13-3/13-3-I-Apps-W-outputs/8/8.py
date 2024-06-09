
n, m = map(int, input().split())
field = [input() for _ in range(n)]

# Check if the field is rectangular
if len(set(len(row) for row in field)) != 1:
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

# Check if the field has three equal-width stripes
if len(field[0]) % 3 != 0:
    print("NO")
    exit()

# Check if the field has three equal-height stripes
if len(field) % 3 != 0:
    print("NO")
    exit()

# Check if the field has parralel stripes
for i in range(0, len(field[0]), 3):
    for j in range(1, len(field)):
        if field[j][i] != field[j-1][i]:
            print("NO")
            exit()

print("YES")

