
def solve(a, b, l, r):
    # Initialize the string with the first a letters of the alphabet
    s = "".join(chr(i + ord('a')) for i in range(a))

    # Mister B's opponent's algorithm
    def opponent_algorithm(suffix):
        # Create a set of letters to choose from
        letters = set(suffix)
        # Generate a string of length a with distinct letters
        t = "".join(chr(i + ord('a')) for i in range(a) if chr(i + ord('a')) not in letters)
        return t

    # Mister B's strategy
    while l <= r:
        # Get the suffix of length a from the current position
        suffix = s[l:l+a]
        # Generate the next string using the opponent's algorithm
        next_string = opponent_algorithm(suffix)
        # Append the next string to the end of s
        s += next_string
        # Increment l and r by b
        l += b
        r += b

    # Return the number of different letters in the segment from l to r, inclusive
    return len(set(s[l-1:r]))

