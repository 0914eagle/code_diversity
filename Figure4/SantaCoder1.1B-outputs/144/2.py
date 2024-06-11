def simplify(x, n):
    
    x = x.split('/')
    x = [int(i) for i in x]
    n = int(n)
    if x[0] * n == n:
        return True
    else:
        return False


if __name__ == '__main__':
    print(simplify("1/5", "5/1"))
    print(simplify("1/6", "2/1"))
    print(simplify("7/10", "10/2"))
