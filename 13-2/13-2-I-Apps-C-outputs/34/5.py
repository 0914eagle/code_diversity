
def solve(a, b, l, r):
    # Initialize the string with the first a letters of the alphabet
    s = "".join(chr(i + ord('a')) for i in range(a))

    # Mister B's opponent's algorithm
    def opponent_algorithm(suffix):
        # Generate all possible strings of length a with distinct letters
        all_strings = ["".join(sorted(suffix + c)) for c in itertools.combinations(string.ascii_lowercase, a)]
        # Find the lexicographically minimal string that is not in the suffix
        for string in all_strings:
            if string not in suffix:
                return string
        return None

    # Mister B's algorithm
    def mister_b_algorithm(l, r):
        # Find the number of different letters in the segment [l, r]
        return len(set(s[l-1:r]))

    # Simulate the game until the segment [l, r] is reached
    while l > len(s):
        # Mister B's opponent moves first
        suffix = s[-a:]
        t = opponent_algorithm(suffix)
        s += t
        # Mister B moves second
        s += "".join(chr(i + ord('a')) for i in range(b))

    # Return the number of different letters in the segment [l, r]
    return mister_b_algorithm(l, r)

