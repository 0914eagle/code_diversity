
def get_maximum_quadrilateral_area(s1, s2, s3, s4):
    
    s = sorted([s1, s2, s3, s4])
    return (s[0] + s[1]) * (s[2] + s[3])

