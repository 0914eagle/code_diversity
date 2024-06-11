def multiply(a, b):
    
    # Your code here
    if a == 0:
        return b
    if b == 0:
        return a
    if a < 0:
        a = -a
    if b < 0:
        b = -b
    if a < b:
        return multiply(a, b)
    if a == b:
        return 1
    return multiply(a, b - 1) + multiply(a - 1, b)

