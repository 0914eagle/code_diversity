
def solve_quadrilateral_problem(s1, s2, s3, s4):
    # Calculate the maximum area of a quadrilateral using Heron's formula
    s = (s1 + s2 + s3 + s4) / 2
    area = (s * (s - s1) * (s - s2) * (s - s3) * (s - s4)) ** 0.5
    return area

