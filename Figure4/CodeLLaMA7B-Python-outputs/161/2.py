def solve(s):
    
    # s = list(s)
    # for i in range(len(s)):
    #     if s[i].isalpha():
    #         if s[i].islower():
    #             s[i] = s[i].upper()
    #         else:
    #             s[i] = s[i].lower()
    # return "".join(s)
    return s.swapcase() if any(c.isalpha() for c in s) else s[::-1]


if __name__ == '__main__':
    print(solve("1234"))
    print(solve("ab"))
    print(solve("#a@C"))
