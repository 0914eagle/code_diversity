
def solve(N, points):
    # Initialize the scores of both players to 0
    score1, score2 = 0, 0
    
    # Iterate through each point and calculate the area of the quadrilateral formed by the point and its neighbors
    for i in range(N):
        x1, y1 = points[i]
        for j in range(i+1, N):
            x2, y2 = points[j]
            area = abs(x1*y2 + x2*y1 - x1*y1 - x2*y2) // 2
            score1 += area
            score2 += area
    
    # Return the sum of the scores modulo 1000003
    return (score1 + score2) % 1000003

