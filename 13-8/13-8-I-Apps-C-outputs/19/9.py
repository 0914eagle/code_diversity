
def solve(a, b, l, r):
    # Initialize the string with the first a letters of the alphabet
    s = "".join(chr(ord('a') + i) for i in range(a))

    # Mister B appends b letters on each move
    for i in range(b):
        # The computer appends a letter that is not in the suffix of length a
        suffix = s[l-1:r]
        letter = chr(ord('a') + a + 1)
        while letter in suffix:
            letter = chr(ord(letter) + 1)
        s += letter

    # Return the number of different letters in the segment from l to r, inclusive
    return len(set(s[l-1:r]))

