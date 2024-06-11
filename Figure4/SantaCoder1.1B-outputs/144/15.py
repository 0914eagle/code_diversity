def simplify(x, n):
    
    x = x.replace("/", "")
    n = n.replace("/", "")
    if x == "0" or n == "0":
        return True
    if x.isdigit() and n.isdigit():
        return int(x) * int(n) == int(x) + int(n)
    if x.isdigit() and n.isalpha():
        return int(x) * int(n) == int(x) + int(n)
    if n.isdigit() and x.isalpha():
        return int(n) * int(x) == int(n) + int(x)
    if x.isdigit() and n.isalpha():
        return int(x) * int(n) == int(x) + int(n)
    if x.isalpha() and n.isdigit():
        return int(x) * int(n) == int(x) + int(n)
    if x.isalpha() and n.isalpha():
        return int(x) * int(n) == int(x) + int(n)
    if x.isalpha() and n.isalpha():
        return int(x) * int(n) == int(x) + int(n)
    return False


if __name__ == "__main__":
    print(simplify("1/5", "5/1"))
    print(simplify("1/6", "2/1"))
    print(simplify("7/10", "10/2"))
    print(simplify("1/5", "5/1"))
    print(simplify("1/6", "2/1"))
    print(simplify("7/10", "10/2"))
    print(simplify("1/5", "5/1"))
    print(simplify("1/6", "2/1"))
    print(simplify("7/10", "10/2"))
    print(simplify("1/5", "5/1"))
    print(simplify("1/6", "2/1"))
    print(simplify("7/10", "10/2"))
    print(simplify("1/5", "5/1"))
    print(simplify("1/6", "2/1"))
    print(simplify("7/10", "10/2"))
    print(simplify("1/5", "5/1"))
   