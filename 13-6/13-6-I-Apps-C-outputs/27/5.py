
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
        if satisfies_pattern(id_list, pattern_list):
            valid_ids += 1

    # Return the number of valid IDs
    return valid_ids

def satisfies_pattern(id_list, pattern_list):
    # Check if the length of the ID is equal to the length of the pattern
    if len(id_list) != len(pattern_list):
        return False

    # Check if the ID satisfies the pattern
    for i in range(len(id_list)):
        if pattern_list[i] == "1" and id_list[i] != "1":
            return False
        if pattern_list[i] == "*" and id_list[i] != "0" and id_list[i] != "1":
            return False

    # If the ID satisfies the pattern, return True
    return True

