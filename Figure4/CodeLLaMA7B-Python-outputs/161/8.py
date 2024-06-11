def solve(s):
    
    if not s.isalpha():
        return s[::-1]
    else:
        return s.swapcase()


if __name__ == '__main__':
    print(solve("1234"))
    print(solve("ab"))
    print(solve("#a@C"))
