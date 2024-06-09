
n = int(input())
b_points = list(map(int, input().split()))

# Create a list to store the points that Bill can choose
bill_points = [0] * (2 * n - 1)

# Initialize the area of the polygon
area = 0

# Iterate through each edge
for i in range(n):
    # Calculate the area of the triangle formed by the points P_i, P_{i+1}, and P_{i+2}
    triangle_area = (b_points[i] + b_points[(i+1)%n] + b_points[(i+2)%n]) / 2
    
    # If the triangle area is greater than the current area, update the area and the corresponding points
    if triangle_area > area:
        area = triangle_area
        bill_points[i*2] = b_points[i]
        bill_points[i*2+1] = b_points[(i+1)%n]
        bill_points[i*2+2] = b_points[(i+2)%n]

# Print the points that Bill should choose
print(*bill_points)

