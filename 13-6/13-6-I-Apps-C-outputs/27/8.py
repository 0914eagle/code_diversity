
def get_max_members(n, pattern):
    # Convert the pattern to a list of 1s and *s
    pattern_list = list(pattern)

    # Initialize a set to store all valid IDs
    valid_ids = set()

    # Iterate over all possible IDs
    for i in range(2**n):
        # Convert the current ID to a binary string
        id_str = bin(i)[2:]
        while len(id_str) < n:
            id_str = '0' + id_str

        # Check if the current ID satisfies the pattern
        if satisfies_pattern(id_str, pattern_list):
            valid_ids.add(id_str)

    # Return the maximum number of members in the agency
    return len(valid_ids)

def satisfies_pattern(id_str, pattern_list):
    # Check if the length of the ID is equal to the length of the pattern
    if len(id_str) != len(pattern_list):
        return False

    # Initialize a counter to keep track of the number of 1s in the ID
    num_ones = 0

    # Iterate over the ID and pattern simultaneously
    for i in range(len(id_str)):
        # Check if the current character in the ID is a 1 or a * in the pattern
        if id_str[i] == '1' or pattern_list[i] == '*':
            num_ones += 1

    # Return True if the number of 1s in the ID is at least half the length of the ID
    return num_ones >= len(id_str) // 2

