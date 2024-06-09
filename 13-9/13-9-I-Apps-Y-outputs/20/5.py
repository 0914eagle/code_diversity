
def solve_quadrilateral(s1, s2, s3, s4):
    
    # Sort the side lengths in descending order
    s = sorted([s1, s2, s3, s4], reverse=True)

    # Find the maximum area of the quadrilateral
    area = (s[0] + s[1] + s[2] + s[3]) * (s[0] + s[1] - s[2] - s[3]) * (s[0] - s[1] + s[2] + s[3]) * (-s[0] + s[1] + s[2] + s[3])
    area = area / 16

    return area

