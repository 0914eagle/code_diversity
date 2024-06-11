def solve(s):
    
    s = s[::-1]
    res = ''
    for c in s:
        if c.isalpha():
            res += c.swapcase()
        else:
            res += c
    return res

