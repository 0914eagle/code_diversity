
def solve(a, b, l, r):
    # Initialize the string s with the first a lowercase English letters in alphabetical order
    s = "".join(chr(i + 97) for i in range(a))

    # Mister B moves first and appends b letters to the string s
    s += "".join(chr(i + 97) for i in range(a, a + b))

    # The opponent adds a letters on each move, so Mister B has to append b letters on each move as well
    while len(s) < r:
        s += "".join(chr(i + 97) for i in range(a + b, a + 2 * b))

    # Count the number of different letters in the segment from position l to position r, inclusive
    return len(set(s[l - 1:r]))

