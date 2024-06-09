
def solve_maximum_quadrilateral_problem(s1, s2, s3, s4):
    # Calculate the perimeter of the quadrilateral
    perimeter = s1 + s2 + s3 + s4
    
    # Calculate the maximum area using Heron's formula
    area = (perimeter * (perimeter - s1) * (perimeter - s2) * (perimeter - s3) * (perimeter - s4)) ** 0.5
    
    return area

