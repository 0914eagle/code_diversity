
n = int(input())

# Initialize the table with ones
table = [[1] * n for _ in range(n)]

# Fill in the remaining elements using the formula
for i in range(1, n):
    for j in range(1, n):
        table[i][j] = table[i - 1][j] + table[i][j - 1]

# Find the maximum value in the table
max_value = max(max(row) for row in table)

print(max_value)

