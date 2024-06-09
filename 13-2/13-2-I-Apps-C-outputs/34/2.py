
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
        # Get the suffix of length a from position l to position r
        suffix = s[l-1:r]
        # Generate a string of length b using the opponent's algorithm
        t = opponent_algorithm(suffix)
        # Append the generated string to the end of s
        s += t
        # Increment l and r by b
        l += b
        r += b

    # Return the number of different letters in the segment from position l to position r, inclusive
    return len(set(s[l-1:r]))
