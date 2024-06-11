def solve(s):
    
    return "".join(map(lambda x: x.upper() if x.isalpha() else x.lower(), s)) if s else s


if __name__ == "__main__":
    print(solve("1234"))
    print(solve("ab"))
    print(solve("#