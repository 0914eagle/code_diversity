
def is_unique_crossword(n, x, encoding):
    # Initialize a set to store the lengths of the segments
    lengths = set()
    # Initialize a variable to store the total length of the crossword
    total_length = 0
    # Iterate through the encoding
    for length in encoding:
        # If the length is not already in the set, add it to the set and increment the total length
        if length not in lengths:
            lengths.add(length)
            total_length += length
    # Check if the total length of the crossword is equal to the chosen length
    if total_length == x:
        # If the number of segments is equal to the number of elements in the encoding, return YES
        if len(lengths) == n:
            return "YES"
        # Otherwise, return NO
        else:
            return "NO"
    # If the total length is not equal to the chosen length, return NO
    else:
        return "NO"

