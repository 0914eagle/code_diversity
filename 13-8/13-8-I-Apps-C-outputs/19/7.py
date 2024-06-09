
def solve(a, b, l, r):
    # Initialize the string with the first a letters of the alphabet
    s = "".join(chr(ord('a') + i) for i in range(a))
    
    # Mister B's opponent's strategy is to append a string of length b that does not contain any letters from the suffix of length a of the string
    while len(s) < r:
        # Find the suffix of length a
        suffix = s[len(s) - a:]
        
        # Generate a string of length b that does not contain any letters from the suffix
        t = "".join(chr(ord('a') + i) for i in range(a, a + b) if chr(ord('a') + i) not in suffix)
        
        # Append the string to the end of s
        s += t
    
    # Return the number of different letters in the segment from position l to position r, inclusive
    return len(set(s[l - 1:r]))

