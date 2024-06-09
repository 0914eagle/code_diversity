
def solve_maximum_quadrilateral_problem(s1, s2, s3, s4):
    # Calculate the perimeter of the quadrilateral
    p = s1 + s2 + s3 + s4
    
    # Calculate the area of the quadrilateral
    area = (s1 * s2 + s2 * s3 + s3 * s4 + s4 * s1) / 2
    
    # Return the maximum area
    return area

