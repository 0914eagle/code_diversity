
# Read input
grid = [list(map(int, input().split())) for _ in range(3)]

# Check if Takahashi's statement is correct
a = [grid[0][0], grid[0][1], grid[0][2]]
b = [grid[0][0], grid[1][0], grid[2][0]]

correct = True
for i in range(3):
    for j in range(3):
        if grid[i][j] != a[i] + b[j]:
            correct = False
            break

# Output the result
if correct:
    print("Yes")
else:
    print("No")
