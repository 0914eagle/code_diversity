
def solve(n, pattern):
    # Convert the pattern to a list of 1s and *s
    pattern_list = list(pattern)

    # Initialize the number of valid IDs to 0
    valid_ids = 0

    # Loop through all possible IDs
    for i in range(2**n):
        # Convert the current ID to a binary string
        id_str = bin(i)[2:]
        id_list = list(id_str.zfill(n))

        # Check if the current ID satisfies the pattern
        if pattern_list[0] == '1' or id_list[0] == '1':
            if pattern_list[1] == '*' or id_list[1] == '1':
                if pattern_list[2] == '1' or id_list[2] == '1':
                    valid_ids += 1

    # Return the number of valid IDs
    return valid_ids

