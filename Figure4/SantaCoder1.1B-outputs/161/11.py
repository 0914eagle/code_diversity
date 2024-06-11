def solve(s):
    
    s = s.lower()
    if not s:
        return s
    if s[0].isalpha():
        s = s[::-1]
    return s


if __name__ == "__main__":
    s = input()
    print(solve(s))
