def solve(s):
    
    s = s.lower()
    if not s:
        return s
    if s[0].isalpha():
        return s[::-1]
    return s[::-1]


if __name__ == "__main__":
    print(solve("1234"))
    print(solve("ab"))
    print(solve("#a