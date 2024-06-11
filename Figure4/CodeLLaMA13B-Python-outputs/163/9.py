def generate_integers(a, b):
    
    if a > b:
        return []
    if a % 2 == 1:
        a += 1
    if b % 2 == 1:
        b -= 1
    return [i for i in range(a, b + 1, 2)]


