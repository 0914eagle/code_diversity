def solve(s):
    
    if not s:
        return s
    s = s.lower()
    for i in range(len(s)):
        if s[i].isalpha():
            s = s[:i] + s[i].upper() + s[i + 1:]
    if s:
        return s[::-1]
    return s
