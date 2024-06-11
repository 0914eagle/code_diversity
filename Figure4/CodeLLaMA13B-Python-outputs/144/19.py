def simplify(x, n):
    
    return eval(x) * eval(n) % 1 == 0


print(simplify("1/5", "5/1"))
print(simplify("1/6", "2/1"))
print(simplify("7/10", "10/2"))
