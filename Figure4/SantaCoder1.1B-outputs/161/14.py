def solve(s):
    
    if not s:
        return s
    if s[0].isalpha():
        return s.upper() if s[0].islower() else s.lower()
    return solve(s[1:])


if __name__ == "__main__":
    print(solve("1234"))
    print(solve("ab"))
    print(solve("#a@C"))
