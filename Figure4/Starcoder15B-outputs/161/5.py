def solve(s):
    
    s = s[::-1]
    for i in range(len(s)):
        if s[i].isalpha():
            s = s[:i] + s[i].swapcase() + s[i+1:]
    return s

