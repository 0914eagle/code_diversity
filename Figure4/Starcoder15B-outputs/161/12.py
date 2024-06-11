def solve(s):
    
    s = list(s)
    for i in range(len(s)):
        if s[i].isalpha():
            s[i] = s[i].swapcase()
    return ''.join(s)


