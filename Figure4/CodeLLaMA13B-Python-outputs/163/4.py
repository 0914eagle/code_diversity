def generate_integers(a, b):
    
    # Your code here
    even_nums = []
    for i in range(a, b + 1):
        if i % 2 == 0:
            even_nums.append(i)
    return even_nums


