
def solve_maximum_quadrilateral_problem(s1, s2, s3, s4):
    # Calculate the maximum area of the quadrilateral
    area = (s1 + s2 + s3 + s4) * (s1 + s2 - s3 - s4) * (s1 - s2 + s3 - s4) * (s1 - s2 - s3 + s4)
    return area ** 0.5

