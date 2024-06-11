def solve(s):
    
    return s.swapcase() if s.isalpha() else s[::-1]


if __name__ == '__main__':
    print(solve("1234"))
    print(solve("ab"))
    print(solve("#a@C"))
