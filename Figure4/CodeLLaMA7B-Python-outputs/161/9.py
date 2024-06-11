def solve(s):
    
    # s = list(s)
    # for i in range(len(s)):
    #     if s[i].isalpha():
    #         if s[i].islower():
    #             s[i] = s[i].upper()
    #         else:
    #             s[i] = s[i].lower()
    # return "".join(s)

    return "".join(c.upper() if c.islower() else c.lower() for c in s if c.isalpha()) or s[::-1]


if