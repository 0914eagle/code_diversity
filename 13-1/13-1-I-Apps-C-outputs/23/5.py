
def solve(N, points):
    # Initialize the scores of both players to 0
    score1, score2 = 0, 0
    
    # Iterate through each point and calculate the area of the quadrilateral formed by the point and its neighbors
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                for l in range(k+1, N):
                    # Calculate the area of the quadrilateral
                    area = abs((points[i][0] * (points[j][1] - points[k][1]) + points[j][0] * (points[k][1] - points[l][1]) + points[k][0] * (points[l][1] - points[i][1]) + points[l][0] * (points[i][1] - points[j][1])) / 2)
                    
                    # Add the area to the score of the current player
                    if i % 2 == 0:
                        score1 += area
                    else:
                        score2 += area
    
    # Return the sum of the scores modulo 1000003
    return (score1 + score2) % 1000003

