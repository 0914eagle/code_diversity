
def get_max_spies(n, pattern):
    # Convert the pattern to a list of 1s and *s
    pattern_list = list(pattern)

    # Initialize the maximum number of spies to 0
    max_spies = 0

    # Loop through all possible IDs
    for i in range(2**n):
        # Convert the current ID to a binary string
        id_str = bin(i)[2:]
        while len(id_str) < n:
            id_str = '0' + id_str

        # Check if the current ID satisfies the pattern
        if satisfies_pattern(id_str, pattern_list):
            # Increment the maximum number of spies
            max_spies += 1

    return max_spies

def satisfies_pattern(id_str, pattern_list):
    # Check if the length of the ID is equal to the length of the pattern
    if len(id_str) != len(pattern_list):
        return False

    # Initialize the number of 1s in the ID to 0
    num_ones = 0

    # Loop through the characters of the ID and pattern
    for i in range(len(id_str)):
        # Check if the current character of the ID is a 1
        if id_str[i] == '1':
            # Increment the number of 1s in the ID
            num_ones += 1

        # Check if the current character of the pattern is a 1
        if pattern_list[i] == '1':
            # Check if the current character of the ID is not a 1
            if id_str[i] != '1':
                # The ID does not satisfy the pattern
                return False

    # Check if the number of 1s in the ID is at least half the length of the ID
    if num_ones < len(id_str) // 2:
        return False

    # The ID satisfies the pattern
    return True

