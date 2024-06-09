
n = int(input())
b_points = list(map(int, input().split()))

# Initialize the points to be chosen
b_1 = b_points[0]
b_2n = b_points[-1]
b_3 = b_points[1]
b_4 = b_points[2]

# Calculate the area of the polygon
area = (n * (n - 3)) / 2

# Calculate the area of the triangle formed by the chosen points
triangle_area = (b_1 * (b_2n - b_3) + b_2n * (b_3 - b_4) + b_3 * (b_4 - b_1)) / 2

# Calculate the area of the triangle formed by the remaining points
remaining_area = area - triangle_area

# Print the points in the order they should be chosen
print(b_1, b_3, b_5)


