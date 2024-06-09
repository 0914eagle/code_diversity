
def solve(n, a, r_1, c_1, r_2, c_2):
    # Calculate the minimum number of times Vasya needs to press the "Down" key to move from line 1 to line n
    down_keys = n - r_1

    # Calculate the minimum number of times Vasya needs to press the "Right" key to move from position 1 to position a_1
    right_keys = a_1 - c_1

    # Calculate the minimum number of times Vasya needs to press the "Left" key to move from position a_n to position c_2
    left_keys = c_2 - 1

    # Return the minimum number of times Vasya needs to press any key
    return down_keys + right_keys + left_keys

