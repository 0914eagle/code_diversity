
def solve(S):
    # Count the number of black and white stones
    black_stones = S.count("B")
    white_stones = S.count("W")

    # The minimum number of new stones needed is the absolute difference between
    # the number of black and white stones
    return abs(black_stones - white_stones)

