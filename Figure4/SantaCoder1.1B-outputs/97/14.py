def multiply(a, b):
    
    # Your code here
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return multiply(a%10, b%10)

