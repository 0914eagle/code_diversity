def solve(s):
    
    if not s:
        return s
    res = []
    for i in s:
        if i.isalpha():
            res.append(i.swapcase())
        else:
            res.append(i)
    return ''.join(res)


if __name__ == '__main__':
    print(solve("1234"))
    print(solve("ab"))
    print(solve("#a@C"))
