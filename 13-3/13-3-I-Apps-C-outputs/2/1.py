
def solve(a, b, l, r):
    # Initialize the string with the first a letters of the alphabet
    s = "".join(chr(i + ord('a')) for i in range(a))

    # Mister B's opponent's algorithm
    def opponent_algorithm(suffix):
        # Generate all possible strings of length a with distinct letters
        all_strings = ["".join(sorted(suffix + c)) for c in itertools.combinations("abcdefghijklmnopqrstuvwxyz", a)]
        # Find the lexicographically minimal string that is not in the suffix
        for string in all_strings:
            if string not in suffix:
                return string
        return ""

    # Mister B's algorithm
    def mister_b_algorithm(l, r):
        # Find the number of different letters in the segment [l, r]
        return len(set(s[l-1:r]))

    # Simulate the game until the segment [l, r] is reached
    while l > len(s) or r > len(s):
        # Mister B's opponent moves first
        suffix = s[-a:]
        opponent_move = opponent_algorithm(suffix)
        s += opponent_move
        # Mister B moves second
        mister_b_move = "a" * b
        s += mister_b_move

    # Return the number of different letters in the segment [l, r]
    return mister_b_algorithm(l, r)

