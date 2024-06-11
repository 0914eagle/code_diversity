def solve(s):
    
    s = s[::-1]
    res = []
    for i in s:
        if i.isalpha():
            res.append(i.swapcase())
        else:
            res.append(i)
    return ''.join(res)


