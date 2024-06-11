def solve(s):
    
    return "".join(reversed(s) if c.isalpha() else c for c in s) if s else s


if __name__ == "__main__":
    print(solve("1234"))
    print(solve("ab"))
    print(solve("#a@C"))
