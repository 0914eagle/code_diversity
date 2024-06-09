
def solve(N, points):
    # Initialize the sum of the scores to 0
    score = 0
    
    # Iterate through each point and calculate the area of the quadrilateral
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                for l in range(k+1, N):
                    # Calculate the area of the quadrilateral
                    area = abs((points[i][0] * points[j][1] + points[j][0] * points[k][1] + points[k][0] * points[l][1] + points[l][0] * points[i][1]) - (points[i][1] * points[j][0] + points[j][1] * points[k][0] + points[k][1] * points[l][0] + points[l][1] * points[i][0])) / 2
                    
                    # Add the area to the score
                    score += area
    
    # Return the sum of the scores modulo 1000003
    return score % 1000003

