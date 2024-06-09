
def solve(a, b, l, r):
    # Initialize the string with the first a letters of the alphabet
    s = "".join(chr(i + ord('a')) for i in range(a))

    # Mister B's turn
    for i in range(b):
        s += chr(i + ord('a'))

    # Compute the number of different letters in the segment [l, r]
    return len(set(s[l-1:r]))

