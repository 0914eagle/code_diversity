def solve(s):
    
    return "".join(map(lambda x: x.lower() if x.isalpha() else x.upper(), s)) if s else s


if __name__ == "__main__":
    print(solve("1234"))
    print(solve("ab"))
    print(solve("#a@C"))
