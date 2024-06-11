def simplify(x, n):
    
    num_x, den_x = x.split("/")
    num_n, den_n = n.split("/")
    return (int(num_x) * int(den_n)) % (int(num_n) * int(den_x)) == 0


# tests
assert simplify("1/5", "5/1")
assert not simplify("1/6", "2/1")
assert not simplify("7/10", "10/2")
