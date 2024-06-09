
def solve(s1, s2, s3, s4):
    # Calculate the perimeter of the quadrilateral
    perimeter = s1 + s2 + s3 + s4
    
    # Calculate the maximum area using the formula: area = (p - a) * (p - b) * (p - c) * (p - d) / 16, where p is the perimeter and a, b, c, and d are the side lengths.
    area = (perimeter - s1) * (perimeter - s2) * (perimeter - s3) * (perimeter - s4) / 16
    
    return area

