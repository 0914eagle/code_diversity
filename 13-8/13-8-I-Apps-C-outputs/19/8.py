
def solve(a, b, l, r):
    # Initialize the string with the first a lowercase English letters
    s = "".join(chr(i + ord('a')) for i in range(a))

    # Mister B appends b letters to the string on each move
    for i in range(b):
        s += chr(i + ord('a'))

    # The opponent appends a letters to the string on each move
    for i in range(a):
        s += chr(i + ord('a'))

    # Count the number of different letters in the segment from l to r, inclusive
    return len(set(s[l-1:r]))

