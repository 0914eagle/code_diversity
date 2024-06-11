def generate_integers(a, b):
    
    # Your code here
    if a > b:
        a, b = b, a
    return [i for i in range(a, b + 1) if i % 2 == 0]


