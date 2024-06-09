
def solve(n, P):
    # Calculate the number of 1s in the pattern
    num_ones = P.count("1")
    # Calculate the number of *s in the pattern
    num_stars = P.count("*")
    # Calculate the total number of characters in the pattern
    total_chars = len(P)
    # Calculate the number of valid IDs
    num_valid_ids = 2**n
    # Initialize the number of members in the agency to 0
    num_members = 0
    # Loop through each possible ID
    for i in range(num_valid_ids):
        # Convert the current ID to a binary string
        binary_string = bin(i)[2:]
        # Pad the binary string with leading 0s to make it the same length as the pattern
        binary_string = binary_string.zfill(n)
        # Check if the binary string satisfies the pattern
        if satisfies_pattern(binary_string, P):
            # Increment the number of members in the agency
            num_members += 1
    # Return the number of members in the agency
    return num_members

def satisfies_pattern(binary_string, P):
    # Check if the length of the binary string is the same as the length of the pattern
    if len(binary_string) != len(P):
        return False
    # Initialize the number of 1s in the binary string to 0
    num_ones = 0
    # Initialize the number of *s in the binary string to 0
    num_stars = 0
    # Loop through each character in the binary string
    for i in range(len(binary_string)):
        # Check if the current character is a 1
        if binary_string[i] == "1":
            # Increment the number of 1s in the binary string
            num_ones += 1
        # Check if the current character is a *
        elif binary_string[i] == "*":
            # Increment the number of *s in the binary string
            num_stars += 1
    # Check if the number of 1s in the binary string is at least half the number of 1s in the pattern
    if num_ones < num_ones / 2:
        return False
    # Check if the number of *s in the binary string is at least half the number of *s in the pattern
    if num_stars < num_stars / 2:
        return False
    # Return True if the binary string satisfies the pattern, False otherwise
    return True

