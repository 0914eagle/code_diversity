
# Read input
grid = [list(map(int, input().split())) for _ in range(3)]

# Check if Takahashi's statement is correct
a_values = set()
b_values = set()

for i in range(3):
    a_values.add(grid[i][0] - grid[i][1])
    b_values.add(grid[0][i] - grid[1][i])

if len(a_values) == 1 and len(b_values) == 1:
    print("Yes")
else:
    print("No")
