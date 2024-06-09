
def solve(a, b, l, r):
    # Initialize the string with the first a letters of the alphabet
    s = "".join(chr(i + ord('a')) for i in range(a))

    # Mister B appends b letters to the string on each move
    for i in range(b):
        # The opponent appends a letters to the string on each move
        s += "".join(chr(i + ord('a')) for i in range(a))

    # Count the number of different letters in the segment from l to r, inclusive
    return len(set(s[l-1:r]))

