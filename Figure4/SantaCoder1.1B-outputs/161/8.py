def solve(s):
    
    return "".join(map(lambda x: x.lower() if x.isalpha() else x.upper(), s)) if s else s


if