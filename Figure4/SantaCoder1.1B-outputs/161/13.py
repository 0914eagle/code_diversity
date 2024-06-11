def solve(s):
    
    return "".join(reversed(s.lower() if c.isalpha() else c) for c in s) if s else s


if __name