def solve(s):
    
    # your code
    if s.isalpha():
        return s.swapcase()
    else:
        return s[::-1]


if __