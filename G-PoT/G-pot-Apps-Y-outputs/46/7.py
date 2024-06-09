
# Read the input grid
grid = [list(map(int, input().split())) for _ in range(3)]

# Check if Takahashi's statement is correct
valid = False
for a1 in range(101):
    for a2 in range(101):
        for a3 in range(101):
            b1 = grid[0][0] - a1
            b2 = grid[0][1] - a2
            b3 = grid[0][2] - a3

            if grid[1][0] == a1 + b1 and grid[1][1] == a2 + b2 and grid[1][2] == a3 + b3:
                if grid[2][0] == a1 + b1 and grid[2][1] == a2 + b2 and grid[2][2] == a3 + b3:
                    valid = True
                    break
        if valid:
            break
    if valid:
        break

# Output the result
if valid:
    print("Yes")
else:
    print("No")
