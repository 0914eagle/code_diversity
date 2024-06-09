
def solve(a, b, c, d):
    # Check if the given conditions are valid
    if a + b + c + d > 10:
        return "impossible"
    
    # Initialize the bit string with all 0s
    bit_string = "0" * (a + b + c + d)
    
    # Fill in the 0s
    for i in range(a):
        bit_string = bit_string[:i] + "0" + bit_string[i:]
    
    # Fill in the 1s
    for i in range(b):
        bit_string = bit_string[:i] + "1" + bit_string[i:]
    
    # Fill in the 01s
    for i in range(c):
        bit_string = bit_string[:i] + "01" + bit_string[i:]
    
    # Fill in the 10s
    for i in range(d):
        bit_string = bit_string[:i] + "10" + bit_string[i:]
    
    return bit_string

