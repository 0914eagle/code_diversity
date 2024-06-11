def solve(s):
    
    # your code here
    # return s
    # return s[::-1]
    # return s.swapcase()
    # return s.swapcase() if s.isalpha() else s[::-1]
    return s.swapcase() if any(c.isalpha() for c in s) else s[::-1]


if __