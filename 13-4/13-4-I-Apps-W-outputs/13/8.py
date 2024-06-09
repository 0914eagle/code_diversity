
n = int(input())

# Initialize a 2D list to store the table
table = [[0] * n for _ in range(n)]

# Fill in the first row and column with ones
for i in range(n):
    table[i][0] = 1
    table[0][i] = 1

# Fill in the remaining elements using the given formula
for i in range(1, n):
    for j in range(1, n):
        table[i][j] = table[i - 1][j] + table[i][j - 1]

# Find the maximum value in the table
max_value = max(max(row) for row in table)

print(max_value)

