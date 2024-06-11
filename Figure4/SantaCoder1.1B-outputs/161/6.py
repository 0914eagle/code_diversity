def solve(s):
    
    return "".join(map(lambda x: x.upper() if x.isalpha() else x.lower(), s)) if s else s
