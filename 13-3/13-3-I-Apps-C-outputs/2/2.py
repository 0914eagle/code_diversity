
def solve(a, b, l, r):
    # Initialize the string with the first a letters of the alphabet
    s = "".join(chr(i + ord('a')) for i in range(a))

    # Mister B's opponent's algorithm
    def opponent_algorithm(suffix):
        # Generate all possible strings of length a with distinct letters
        all_strings = ["".join(sorted(suffix + c)) for c in itertools.combinations("abcdefghijklmnopqrstuvwxyz", a)]
        # Return the lexicographically minimal string
        return min(all_strings)

    # Mister B's algorithm
    def mister_b_algorithm(suffix):
        # Generate all possible strings of length b with distinct letters
        all_strings = ["".join(sorted(suffix + c)) for c in itertools.combinations("abcdefghijklmnopqrstuvwxyz", b)]
        # Return the lexicographically minimal string
        return min(all_strings)

    # Simulate the game until the segment [l, r] is reached
    while l + a - 1 <= r:
        # Get the suffix of length a from the current position
        suffix = s[l:l + a]
        # Get the next string to append to s using Mister B's algorithm
        next_string = mister_b_algorithm(suffix)
        # Get the next string to append to s using the opponent's algorithm
        opponent_string = opponent_algorithm(suffix)
        # Append the next string to s
        s += next_string
        # Update l and r to reflect the new position
        l += a
        r += a

    # Return the number of different letters in the segment [l, r]
    return len(set(s[l:r + 1]))

