def choose_num(x, y):
    
    # Your code here
    for i in range(y, x-1, -1):
        if i % 2 == 0:
            return i
    return -1

# Test cases
print(choose