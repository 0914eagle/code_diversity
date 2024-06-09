
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

    # Mister B's algorithm
    def mister_b_algorithm(suffix):
        # Generate a string of length b with distinct letters
        t = "".join(chr(i + ord('a')) for i in range(b) if chr(i + ord('a')) not in suffix)
        return t

    # Simulate the game until the segment [l, r] is reached
    while l > len(s):
        # Mister B's opponent moves first
        suffix = s[-a:]
        t = opponent_algorithm(suffix)
        s += t
        # Mister B moves
        suffix = s[-a:]
        t = mister_b_algorithm(suffix)
        s += t

    # Return the number of different letters in the segment [l, r]
    return len(set(s[l-1:r]))

