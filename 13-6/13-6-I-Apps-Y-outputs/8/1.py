
def solve_quadrilateral_problem(s1, s2, s3, s4):
    # Sort the side lengths in descending order
    sides = sorted([s1, s2, s3, s4], reverse=True)
    # Calculate the area of the quadrilateral
    area = sides[0] * sides[1]
    return area

