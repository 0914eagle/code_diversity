def solve(s):
    
    # your code here
    # return "".join([c.upper() if c.islower() else c.lower() for c in s])
    # return "".join([c.swapcase() for c in s])
    # return s.swapcase() if s.isalpha() else s[::-1]
    return s.swapcase() if any(c.isalpha() for c in s) else s[::-1]


if __name__ == '__