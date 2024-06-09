
def get_maximum_quadrilateral_area(s1, s2, s3, s4):
    s = [s1, s2, s3, s4]
    s.sort()
    return (s[0] + s[1]) * (s[2] + s[3])

