
def solve(strings, b):
    # Initialize a set to store the unique substrings of b
    unique_substrings = set()
    # Iterate through each string in the pile
    for string in strings:
        # Iterate through each substring of b
        for i in range(len(b)):
            # Check if the substring is present in the string
            if b[i:i+len(string)] == string:
                # If it is, add it to the set of unique substrings
                unique_substrings.add(string)
    # Return the length of the set, which is the number of unique substrings
    return len(unique_substrings)

