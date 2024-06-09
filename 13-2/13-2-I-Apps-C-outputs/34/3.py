
def solve(a, b, l, r):
    # Initialize the string with the first a letters of the alphabet
    s = "".join(chr(i + ord('a')) for i in range(a))

    # Mister B's opponent's algorithm
    def opponent_algorithm(suffix):
        # Create a set of all letters in the suffix
        letter_set = set(suffix)
        # Generate a string of length a with distinct letters not in the suffix
        t = "".join(chr(i + ord('a')) for i in range(a) if chr(i + ord('a')) not in letter_set)
        return t

    # Mister B's algorithm
    def mister_b_algorithm(suffix):
        # Generate a string of length b with distinct letters not in the suffix
        t = "".join(chr(i + ord('a')) for i in range(b) if chr(i + ord('a')) not in suffix)
        return t

    # Simulate the game until the segment [l, r] is reached
    while l + b - 1 <= r:
        # Get the suffix of length a from the current position
        suffix = s[l:l + a]
        # Get the opponent's move
        t = opponent_algorithm(suffix)
        # Append the opponent's move to the string
        s += t
        # Get Mister B's move
        t = mister_b_algorithm(suffix)
        # Append Mister B's move to the string
        s += t
        # Update the position of the segment
        l += b

    # Return the number of different letters in the segment
    return len(set(s[l:r + 1]))

