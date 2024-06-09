
def solve_maximum_quadrilateral_problem(s1, s2, s3, s4):
    # Calculate the maximum area of the quadrilateral
    area = 0.5 * abs(s1 * s2 - s3 * s4)
    
    # Return the maximum area
    return area

