
# Read input
grid = [list(map(int, input().split())) for _ in range(3)]

# Check if Takahashi is correct
a1 = grid[0][0]
b1 = grid[0][1]
c1 = grid[0][2]

a2 = grid[1][0]
b2 = grid[1][1]
c2 = grid[1][2]

a3 = grid[2][0]
b3 = grid[2][1]
c3 = grid[2][2]

if a1 + b1 == c1 and a1 + b2 == c2 and a1 + b3 == c3 and a2 + b1 == c1 and a2 + b2 == c2 and a2 + b3 == c3 and a3 + b1 == c1 and a3 + b2 == c2 and a3 + b3 == c3:
    print("Yes")
else:
    print("No")
