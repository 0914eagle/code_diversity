
def solve(a, b, l, r):
    # Initialize the string with the first a letters of the alphabet
    s = "".join(chr(i + ord('a')) for i in range(a))

    # Mister B's turn
    s += "".join(chr(i + ord('a')) for i in range(a, a + b))

    # Compute the number of different letters in the segment [l, r]
    return len(set(s[l - 1:r]))

