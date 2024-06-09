
def solve(a, b, l, r):
    # Initialize the string s with the first a lowercase English letters in alphabetical order
    s = "".join(chr(ord('a') + i) for i in range(a))

    # Mister B moves first and appends b letters to the string s
    s += "".join(chr(ord('a') + i) for i in range(a, a + b))

    # The opponent adds a letters on each move and appends them to the end of the string s
    while len(s) < r:
        # Generate a string t of length a such that all letters in the string t are distinct and don't appear in the considered suffix
        t = "".join(chr(ord('a') + i) for i in range(a) if chr(ord('a') + i) not in s[-a:])

        # Append the string t to the end of s
        s += t

    # Return the minimum number of different letters in the segment from position l to position r, inclusive
    return len(set(s[l - 1:r]))

