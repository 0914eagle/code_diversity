def generate_integers(a, b):
    
    # Your code here
    if a > b:
        return []
    if a % 2 != 0:
        a += 1
    if b % 2 != 0:
        b -= 1
    return list(range(a, b + 1, 2))


print(generate_integers(2, 8))
print(generate_integers(8, 2))
print(generate_integers(10, 14))
