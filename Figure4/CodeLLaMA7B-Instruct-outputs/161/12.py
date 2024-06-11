

def solve(s):
    
    # Check if the string contains any letters
    if any(c.isalpha() for c in s):
        # If it contains letters, reverse the case of the letters
        return ''.join(c.lower() if c.isupper() else c.upper() for c in s)
    else:
        # If it does not contain letters, reverse the string
        return s[::-1]


