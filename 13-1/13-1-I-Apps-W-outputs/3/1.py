
n, m, k, q = map(int, input().split())

broken_pixels = []
for i in range(q):
    x, y, t = map(int, input().split())
    broken_pixels.append((x, y, t))

# Sort the broken pixels by their time of failure
broken_pixels.sort(key=lambda x: x[2])

# Initialize the matrix with all pixels working
matrix = [[0 for _ in range(m)] for _ in range(n)]

# Loop through the broken pixels and mark the corresponding pixels as broken
for x, y, t in broken_pixels:
    matrix[x-1][y-1] = t

# Check if there is a square of size k × k with all broken pixels
for i in range(n-k+1):
    for j in range(m-k+1):
        if all(matrix[i+x][j+y] > 0 for x in range(k) for y in range(k)):
            print(matrix[i+k-1][j+k-1])
            return

print(-1)

