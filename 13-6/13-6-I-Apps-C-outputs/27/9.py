
def get_max_spies(n, pattern):
    # Initialize a set to store all valid IDs
    valid_ids = set()

    # Iterate over all possible IDs of length n
    for id in range(1, 2**n):
        # Convert the ID to binary string
        id_str = bin(id)[2:]
        id_str = '0' * (n - len(id_str)) + id_str

        # Check if the ID satisfies the pattern
        if satisfies_pattern(id_str, pattern):
            # If the ID satisfies the pattern, add it to the set of valid IDs
            valid_ids.add(id_str)

    # Return the maximum number of spies that can be employed
    return len(valid_ids)

def satisfies_pattern(id_str, pattern):
    # Initialize a variable to store the number of 1s in the ID
    num_ones = id_str.count('1')

    # Iterate over the characters of the pattern
    for i, char in enumerate(pattern):
        # If the character is a 1, decrease the number of 1s in the ID
        if char == '1':
            num_ones -= 1

        # If the number of 1s in the ID becomes negative, return False
        if num_ones < 0:
            return False

        # If the character is a *, return True
        if char == '*':
            return True

    # If the pattern is exhausted and the number of 1s in the ID is non-negative, return True
    return num_ones >= 0

