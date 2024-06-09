
def count_unique_substrings(strings, substring):
    # Initialize a set to store the unique substrings
    unique_substrings = set()
    
    # Iterate over the strings in the pile
    for string in strings:
        # Iterate over the characters in the string
        for i in range(len(string)):
            # Check if the substring is present in the string
            if string[i:i+len(substring)] == substring:
                # Add the substring to the set of unique substrings
                unique_substrings.add(substring)
    
    # Return the number of unique substrings
    return len(unique_substrings)

