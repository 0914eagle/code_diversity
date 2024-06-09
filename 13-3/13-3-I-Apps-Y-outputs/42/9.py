
x1, y1, x2, y2 = map(int, input().split())

# Calculate the slope of the line passing through (x1, y1) and (x2, y2)
m = (y2 - y1) / (x2 - x1)

# Calculate the coordinates of the third vertex
x3 = x2 - y2 + y1
y3 = y2 + x2 - x1

# Calculate the coordinates of the fourth vertex
x4 = x3 - y3 + y1
y4 = y3 + x3 - x1

# Print the coordinates of the third and fourth vertices
print(x3, y3, x4, y4)

