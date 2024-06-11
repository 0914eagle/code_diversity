def generate_integers(a, b):
    
    if a > b:
        return generate_integers(b, a)
    if a % 2 == 1:
        a += 1
    if b % 2 == 0:
        b -= 1
    return [x for x in range(a, b + 1, 2)]


