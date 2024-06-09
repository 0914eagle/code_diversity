
def solve_maximum_quadrilateral_problem(s1, s2, s3, s4):
    
    # Sort the side lengths in descending order
    sides = sorted([s1, s2, s3, s4], reverse=True)

    # Use the formula for the area of a triangle
    # to find the area of the triangle with the largest perimeter
    area = 0.5 * (sides[0] + sides[1] + sides[2]) * sides[3]

    return area

