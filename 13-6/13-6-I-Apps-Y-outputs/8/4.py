
def solve_maximum_quadrilateral_problem(s1, s2, s3, s4):
    
    # Sort the side lengths in descending order
    s = sorted([s1, s2, s3, s4], reverse=True)

    # Calculate the area of the quadrilateral
    area = 0.5 * (s[0] * s[1] + s[1] * s[2] + s[2] * s[3] + s[3] * s[0])

    return area

