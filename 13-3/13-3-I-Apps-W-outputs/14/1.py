
n = int(input())
b = list(map(int, input().split()))

# Initialize the points to be chosen
points = [0] * (2 * n)

# Choose the points in such a way that the area of the polygon is maximized
for i in range(n):
    # Choose the point on the ith edge that is closest to the midpoint of the edge
    points[2 * i] = (b[i] + (n - 1) - b[i]) // 2

# Print the chosen points
print(*points)

