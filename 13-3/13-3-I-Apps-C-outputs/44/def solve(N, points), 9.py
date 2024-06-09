
def solve(N, points):
    # Calculate the area of the quadrilateral
    area = abs(points[0][0] * points[1][1] + points[1][0] * points[2][1] + points[2][0] * points[3][1] + points[3][0] * points[0][1] - points[0][1] * points[1][0] - points[1][1] * points[2][0] - points[2][1] * points[3][0] - points[3][1] * points[0][0]) / 2
    
    # Calculate the sum of the scores
    score = area * 2
    
    # Return the sum of the scores modulo 1000003
    return score % 1000003

