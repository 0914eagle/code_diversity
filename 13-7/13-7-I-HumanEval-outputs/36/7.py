
def solve(s: str) -> str:
    
    # Check if the string contains any letters
    if any(c.isalpha() for c in s):
        # If it contains letters, reverse the case of all letters
        return ''.join(c.lower() if c.isupper() else c.upper() for c in s)
    else:
        # If it contains no letters, reverse the string
        return s[::-1]

