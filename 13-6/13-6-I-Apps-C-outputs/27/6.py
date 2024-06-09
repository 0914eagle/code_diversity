
def get_max_members(n, pattern):
    # Convert the pattern to a list of 1s and *s
    pattern_list = list(pattern)

    # Initialize a counter for the number of 1s in the pattern
    num_ones = 0

    # Iterate through the pattern list and count the number of 1s
    for char in pattern_list:
        if char == "1":
            num_ones += 1

    # Calculate the maximum number of members based on the length of the ID and the number of 1s in the pattern
    max_members = 2 ** n
    if num_ones < n:
        max_members -= 2 ** (n - num_ones)

    return max_members

