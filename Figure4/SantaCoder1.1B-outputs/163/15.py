def generate_integers(a, b):
    
    if a > b:
        return []
    if a == b:
        return [a]
    if a == 0:
        return []
    if b == 0:
        return []
    if a % 2 == 0:
        return generate_integers(a // 2, b)
    else:
        return generate_integers(a // 2, b) + [a]


