
def solve(a, b, c, d):
    # Check if the given conditions are valid
    if a + b + c + d > 10:
        return "impossible"
    
    # Initialize the bit string with all 0s
    bit_string = "0" * (a + b + c + d)
    
    # Insert 0s to form the subsequence 00
    for i in range(a):
        bit_string = bit_string[:i] + "0" + bit_string[i:]
    
    # Insert 1s to form the subsequence 01
    for i in range(a, a + b):
        bit_string = bit_string[:i] + "1" + bit_string[i:]
    
    # Insert 0s to form the subsequence 10
    for i in range(a + b, a + b + c):
        bit_string = bit_string[:i] + "0" + bit_string[i:]
    
    # Insert 1s to form the subsequence 11
    for i in range(a + b + c, a + b + c + d):
        bit_string = bit_string[:i] + "1" + bit_string[i:]
    
    return bit_string

