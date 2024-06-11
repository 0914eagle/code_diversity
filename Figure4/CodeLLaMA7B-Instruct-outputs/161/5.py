

def solve(s):
    
    # Check if the string contains any letters
    if any(c.isalpha() for c in s):
        # If it contains letters, reverse the case of the letters
        return ''.join(c.swapcase() if c.isalpha() else c for c in s)
    else:
        # If it does not contain letters, reverse the string
        return s[::-1]


