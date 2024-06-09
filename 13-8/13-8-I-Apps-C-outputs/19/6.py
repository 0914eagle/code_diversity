
def solve(a, b, l, r):
    # Initialize the string with the first a lowercase English letters
    s = ''.join(chr(i + ord('a')) for i in range(a))

    # Mister B's opponent is a computer that generates a string t of length a
    # such that all letters in the string t are distinct and don't appear in the considered suffix
    def generate_string(suffix):
        t = ''
        while len(t) < a:
            c = chr(ord('a') + a - 1)
            if c not in suffix and c not in t:
                t += c
        return t

    # Mister B moves first and appends b letters to the string
    s += ''.join(chr(ord('a') + i) for i in range(b))

    # The opponent moves and appends a letters to the string
    s += generate_string(s[l:r])

    # Return the minimum number of different letters in the segment from position l to position r, inclusive
    return len(set(s[l:r]))

