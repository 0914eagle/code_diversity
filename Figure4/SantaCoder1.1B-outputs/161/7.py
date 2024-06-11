def solve(s):
    
    if not s:
        return s
    if s[0].isalpha():
        return solve(s[1:])
    else:
        return solve(s[1:] + s[0].lower())


if __name__ == "__main__":
    print(solve("1234"))
    print(solve("ab"))
    print(solve("#a@C"))
