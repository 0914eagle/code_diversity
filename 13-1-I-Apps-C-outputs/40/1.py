
def solve(n, pattern):
    # Convert the pattern to a list of 1s and *s
    pattern_list = list(pattern)

    # Initialize the maximum number of members to 0
    max_members = 0

    # Loop through all possible IDs
    for i in range(2**n):
        # Convert the current ID to a binary string
        id_str = bin(i)[2:]
        while len(id_str) < n:
            id_str = '0' + id_str

        # Check if the current ID satisfies the pattern
        if satisfies_pattern(id_str, pattern_list):
            max_members += 1

    return max_members

def satisfies_pattern(id_str, pattern_list):
    # Check if the length of the ID is equal to the length of the pattern
    if len(id_str) != len(pattern_list):
        return False

    # Check if the ID satisfies the pattern
    for i in range(len(id_str)):
        if pattern_list[i] == '1' and id_str[i] != '1':
            return False
        if pattern_list[i] == '*' and id_str[i] != '0' and id_str[i] != '1':
            return False

    return True

