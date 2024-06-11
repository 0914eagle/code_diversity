def digits(n):
    
    # Your code here
    odd_product = 1
    for i in str(n):
        if int(i) % 2 != 0:
            odd_product *= int(i)
    return odd_product

# 2