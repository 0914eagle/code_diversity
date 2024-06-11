def simplify(x, n):
    
    num1, den1 = x.split("/")
    num2, den2 = n.split("/")
    return (int(num1) * int(den2)) % (int(num2) * int(den1)) == 0


print(simplify("1/5", "5/1"))
print(simplify("1/6", "2/1"))
print(simplify("7/10", "10/2"))
