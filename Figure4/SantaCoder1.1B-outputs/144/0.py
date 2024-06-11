def simplify(x, n):
    
    x = x.replace("/", "")
    n = n.replace("/", "")
    x = x.split("/")
    n = n.split("/")
    if len(x) != 2 or len(n) != 2:
        return False
    if x[0].isdigit() and x[1].isdigit() and n[0].isdigit() and n[1].isdigit():
        x = int(x[0]) / int(x[1])
        n = int(n[0]) / int(n[1])
        if x * n == int(x * n):
            return True
    return False


if __name__ == "__main__":
    print(simplify("1/5", "5/1"))
    print(simplify("1/6", "2/1"))
    print(simplify("7/10", "10/2"))
