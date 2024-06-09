
def solve(a, b, l, r):
    # Initialize the string with the first a lowercase English letters in alphabetical order
    s = "".join(chr(ord('a') + i) for i in range(a))

    # Mister B appends b letters on each move
    for i in range(b):
        # The opponent appends a letters on each move
        s += "".join(chr(ord('a') + i) for i in range(a))

    # The opponent's suffix is the substring of s from positions l to r, inclusive
    suffix = s[l-1:r]

    # Create a set to store the unique letters in the suffix
    unique_letters = set()

    # Iterate through the suffix and add each letter to the set
    for letter in suffix:
        unique_letters.add(letter)

    # Return the length of the unique letters set, which is the minimum number of different letters in the segment
    return len(unique_letters)

