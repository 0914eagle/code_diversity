


def count_distinct_characters(string: str) -> int:
    
    # Convert the string to lowercase
    string = string.lower()
    # Create a set to store the distinct characters
    distinct_chars = set()
    # Loop through each character in the string
    for char in string:
        # If the character is not in the set, add it
        if char not in distinct_chars:
            distinct_chars.add(char)
    # Return the length of the set, which is the number of distinct characters
    return len(distinct_chars)


