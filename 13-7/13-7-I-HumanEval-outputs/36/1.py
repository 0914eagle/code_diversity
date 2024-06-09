
def solve(s: str) -> str:
    
    # Check if the string contains any letters
    if any(c.isalpha() for c in s):
        # If it does, reverse the case of all letters
        return ''.join(c.swapcase() if c.isalpha() else c for c in s)
    else:
        # If it doesn't, reverse the string
        return s[::-1]

