def generate_integers(a, b):
    
    # Your code here
    result = []
    for i in range(a, b + 1):
        if i % 2 == 0:
            result.append(i)
    return result


