def generate_integers(a, b):
    
    if a > b:
        return generate_integers(b, a)
    elif a % 2 != 0:
        a += 1
    elif b % 2 != 0:
        b -= 1
    return [x for x in range(a, b + 1, 2)]


