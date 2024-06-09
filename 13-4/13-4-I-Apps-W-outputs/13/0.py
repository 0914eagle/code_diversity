
n = int(input())

# Initialize a 2D array with ones
a = [[1] * n for _ in range(n)]

# Fill in the remaining elements using the formula
for i in range(1, n):
    for j in range(1, n):
        a[i][j] = a[i - 1][j] + a[i][j - 1]

# Find the maximum value in the table
m = max(max(row) for row in a)

print(m)

