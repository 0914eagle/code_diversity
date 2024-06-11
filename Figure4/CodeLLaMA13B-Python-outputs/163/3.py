def generate_integers(a, b):
    
    # Your code here
    even_ints = []
    for i in range(a, b + 1):
        if i % 2 == 0:
            even_ints.append(i)
    return even_ints


