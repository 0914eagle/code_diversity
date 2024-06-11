def generate_integers(a, b):
    
    # Your code here
    if a > b:
        return generate_integers(b, a)
    else:
        return [x for x in range(a, b + 1) if x % 2 == 0]


print(generate_integers(2, 8))
print(generate_integers(8, 2))
print(generate_integers(10, 14))
