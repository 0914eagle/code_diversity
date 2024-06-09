
def count_unique_substrings(strings, substring):
    # Initialize a set to store the unique substrings
    unique_substrings = set()
    
    # Iterate over each string in the pile
    for string in strings:
        # Iterate over each substring of the current string
        for i in range(len(string)):
            # Check if the substring is present in the pile
            if string[i:i+len(substring)] == substring:
                # If it is, add it to the set of unique substrings
                unique_substrings.add(substring)
    
    # Return the number of unique substrings
    return len(unique_substrings)

