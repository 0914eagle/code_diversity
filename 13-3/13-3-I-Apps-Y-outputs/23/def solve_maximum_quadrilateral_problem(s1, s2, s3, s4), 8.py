
def solve_maximum_quadrilateral_problem(s1, s2, s3, s4):
    # Sort the side lengths in descending order
    sides = sorted([s1, s2, s3, s4], reverse=True)

    # Initialize the maximum area
    max_area = 0

    # Iterate over all possible combinations of side lengths
    for i in range(4):
        for j in range(i+1, 4):
            for k in range(j+1, 4):
                l = 4 - i - j - k
                area = sides[i] * sides[j] * sides[k] * sides[l]
                max_area = max(max_area, area)

    return max_area

