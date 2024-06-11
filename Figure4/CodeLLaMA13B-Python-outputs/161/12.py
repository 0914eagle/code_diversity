def solve(s):
    
    # your code here
    # return "".join(c.lower() if c.isupper() else c.upper() for c in s)
    # return "".join(c.swapcase() if c.isalpha() else c for c in s)
    return s.swapcase() if s.isalpha() else s[::-1]


if