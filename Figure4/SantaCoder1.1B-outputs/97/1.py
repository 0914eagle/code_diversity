def multiply(a, b):
    
    # Write your code here
    a = str(a)
    b = str(b)
    a = a[::-1]
    b = b[::-1]
    product = 0
    for i in range(len(a)):
        if a[i] == b[i]:
            product += int(a[i]) * int(b[i])
    return product

