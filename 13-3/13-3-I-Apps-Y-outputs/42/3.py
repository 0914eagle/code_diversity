
x1, y1, x2, y2 = map(int, input().split())

# Calculate the slope of the line passing through (x1, y1) and (x2, y2)
slope = (y2 - y1) / (x2 - x1)

# Calculate the coordinates of the third vertex
x3 = x1 + (y2 - y1) / slope
y3 = y1 + (x2 - x1) * slope

# Calculate the coordinates of the fourth vertex
x4 = x2 + (y2 - y1) / slope
y4 = y2 + (x2 - x1) * slope

# Print the coordinates of the third and fourth vertices
print(int(x3), int(y3), int(x4), int(y4))

