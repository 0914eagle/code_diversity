
def solve(s: str) -> str:
    
    # Check if the string contains any letters
    if any(c.isalpha() for c in s):
        # If it does, reverse the case of the letters
        return ''.join(c.lower() if c.isupper() else c.upper() for c in s)
    else:
        # If it doesn't, reverse the string
        return s[::-1]

