
x1, y1, x2, y2 = map(int, input().split())

# Calculate the slope of the line passing through (x1, y1) and (x2, y2)
m = (y2 - y1) / (x2 - x1)

# Calculate the x-coordinate of the third vertex
x3 = x1 + (y2 - y1) / m

# Calculate the y-coordinate of the third vertex
y3 = y1 + m * (x3 - x1)

# Calculate the x-coordinate of the fourth vertex
x4 = x2 + (y2 - y1) / m

# Calculate the y-coordinate of the fourth vertex
y4 = y2 + m * (x4 - x2)

# Print the coordinates of the third and fourth vertices
print(int(x3), int(y3), int(x4), int(y4))

