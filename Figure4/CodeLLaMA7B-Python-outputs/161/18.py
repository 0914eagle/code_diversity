def solve(s):
    
    # s = list(s)
    # for i in range(len(s)):
    #     if s[i].isalpha():
    #         s[i] = s[i].swapcase()
    # return "".join(s)
    return "".join(c.swapcase() if c.isalpha() else c for c in s)


if __name__ == "__main__":