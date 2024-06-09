
def solve(N, points):
    # Initialize the sum of the scores to 0
    score = 0
    
    # Iterate over each point in the input
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                for l in range(k+1, N):
                    # Check if the points form a quadrilateral
                    if is_quadrilateral(points[i], points[j], points[k], points[l]):
                        # Add the area of the quadrilateral to the score
                        score += area_quadrilateral(points[i], points[j], points[k], points[l])
    
    # Return the sum of the scores modulo 1000003
    return score % 1000003

# Check if the points form a quadrilateral
def is_quadrilateral(p1, p2, p3, p4):
    return (p1[0] != p2[0] or p1[1] != p2[1]) and (p2[0] != p3[0] or p2[1] != p3[1]) and (p3[0] != p4[0] or p3[1] != p4[1]) and (p4[0] != p1[0] or p4[1] != p1[1])

# Calculate the area of a quadrilateral
def area_quadrilateral(p1, p2, p3, p4):
    return abs((p1[0] * (p2[1] - p3[1]) + p2[0] * (p3[1] - p4[1]) + p3[0] * (p4[1] - p1[1]) + p4[0] * (p1[1] - p2[1])) / 2.0)

