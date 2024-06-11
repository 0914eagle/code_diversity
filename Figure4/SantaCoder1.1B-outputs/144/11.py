def simplify(x, n):
    
    x = x.replace("/", "")
    n = n.replace("/", "")
    x = x.split("/")
    n = n.split("/")
    if len(x) != 2 or len(n) != 2:
        return False
    if int(x[0]) == 0 or int(n[0]) == 0:
        return False
    if int(x[1]) == 1:
        return int(n[1]) == 1
    if int(n[1]) == 1:
        return int(x[1]) == 1
    if int(x[0]) == 1:
        return int(n[1]) == int(x[1])
    if int(n[0]) == 1:
        return int(x[1]) == int(n[1])
    if int(x[0]) == 2:
        return int(n[1]) == int(x[1])
    if int(n[0]) == 2:
        return int(x[1]) == int(n[1])
    if int(x[0]) == 3:
        return int(n[1]) == int(x[1])
    if int(n[0]) == 3:
        return int(x[1]) == int(n[1])
    if int(x[0]) == 4:
        return int(n[1]) == int(x[1])
    if int(n[0]) == 4:
        return int(x[1]) == int(n[1])
    if int(x[0]) == 5:
        return int(n[1]) == int(x[1])
    if int(n[0]) == 5:
        return int(x[1]) == int(n[1])
    if int(x[0]) == 6:
        return int(n[1]) == int(x[1])
    if int(n[0]) == 6:
        return int(x[1]) == int(n[1])
    if int(x[0]) == 7:
        return int(n[1]) == int(x[1])
    if int(n[0]) == 7:
        return int(x[1]) == int(n[1])
    if int(x[0]) == 8: