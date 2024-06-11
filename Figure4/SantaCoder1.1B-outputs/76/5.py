def is_simple_power(x, n):
    
    return n**int(x) == x

# Test cases
assert is_simple_power(1, 4) == True
assert is_simple_power(2, 2) == True
assert is_