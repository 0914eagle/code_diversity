def solve(s):
    
    if not s:
        return s
    if s[0].isalpha():
        return solve(s.lower())[::-1]
    else:
        return solve(s.upper())[::-1]
