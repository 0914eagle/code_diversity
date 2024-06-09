
def find_max_area(s1, s2, s3, s4):
    # Sort the side lengths in descending order
    sides = sorted([s1, s2, s3, s4], reverse=True)
    # Find the maximum area
    area = sides[0] * sides[1]
    return area

