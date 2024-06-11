def simplify(x, n):
    
    if x == "0":
        return True
    if x == "1":
        return False
    if x.count("/") == 1:
        numerator, denominator = x.split("/")
        if int(numerator) == 0:
            return False
        if int(denominator) == 1:
            return True
        if int(denominator) == 0:
            return False
        return simplify(numerator, int(denominator))
    if x.count("/") == 2:
        numerator, denominator = x.split("/")
        if int(numerator) == 0:
            return False
        if int(denominator) == 1:
            return False
        if int(denominator) == 0:
            return False
        return simplify(numerator, int(denominator))
    if x.count("/") == 3:
        numerator, denominator = x.split("/")
        if int(numerator) == 0:
            return False
        if int(denominator) == 1:
            return False
        if int(denominator) == 0:
            return False
        return simplify(numerator, int(denominator))
    if x.count("/") == 4:
        numerator, denominator = x.split("/")
        if int(numerator) == 0:
            return False
        if int(denominator) == 1:
            return False
        if int(denominator) == 0:
            return False
        return simplify(numerator, int(denominator))
    if x.count("/") == 5:
        numerator, denominator = x.split("/")
        if int(numerator) == 0:
            return False
        if int(denominator) == 1:
            return False
        if int(denominator) == 0:
            return False
        return simplify(numerator, int(denominator))
    if x.count("/") == 6:
        numerator, denominator = x.split("/")
        if int(numerator) == 0:
            return False
        if int(denominator) == 1:
            return False
        if int(denominator) == 0:
            return False
        return simplify(numerator, int(denominator))
    if x.count("/") == 7:
        numerator, denominator = x.split("/")
        if int(numerator) == 0:
            return False
        if int(denominator) == 1:
            return False
        if int(denominator) == 0:
            return False
        return simplify(numerator, int(denominator))
    if x.count("/") == 8:
        numerator, denominator = x