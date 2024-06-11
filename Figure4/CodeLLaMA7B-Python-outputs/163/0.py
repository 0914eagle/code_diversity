def generate_integers(a, b):
    
    # Your code here
    if a > b:
        a, b = b, a
    return [x for x in range(a, b + 1, 2) if x % 10 == 0]


