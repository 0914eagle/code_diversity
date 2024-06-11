def simplify(x, n):
    
    num1, den1 = x.split("/")
    num2, den2 = n.split("/")
    return (int(num1) * int(den2)) % (int(num2) * int(den1)) == 0


# tests
