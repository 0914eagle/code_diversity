def solve(s):
    
    res = ''
    for i in s:
        if i.isalpha():
            res += i.swapcase()
        else:
            res += i
    return res[::-1]


