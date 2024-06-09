
def solve(a, b, c, d):
    # Check if the given conditions are valid
    if a + b + c + d > 10:
        return "impossible"
    
    # Initialize the bit string with all 0s
    bit_string = "0" * (a + b + c + d)
    
    # Add 0s to the bit string to make the subsequence 00 occur a times
    for i in range(a):
        bit_string += "00"
    
    # Add 1s to the bit string to make the subsequence 01 occur b times
    for i in range(b):
        bit_string += "01"
    
    # Add 1s to the bit string to make the subsequence 10 occur c times
    for i in range(c):
        bit_string += "10"
    
    # Add 1s to the bit string to make the subsequence 11 occur d times
    for i in range(d):
        bit_string += "11"
    
    return bit_string

