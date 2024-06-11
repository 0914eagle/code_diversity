def simplify(x, n):
    
    x = x.replace("/", "")
    n = n.replace("/", "")
    if x == "0" or n == "0":
        return True
    if x == "1" or n == "1":
        return True
    if x == "0" or n == "0":
        return True
    if x.isdigit() and n.isdigit():
        x = int(x)
        n = int(n)
        if x * n == 1:
            return True
        if x * n == 0:
            return False
    return False


if __name__ == "__main__":
    print(simplify("1/5", "5/1"))
    print(simplify("1/6", "2/1"))
    print(simplify("7/10", "10/2"))
