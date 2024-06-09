
def solve(N, b):
    # Check if N is within the required range
    if N < 1 or N > 10**15:
        return "no"
    
    # Check if b is within the required range
    if b < 0 or b > 50:
        return "no"
    
    # Calculate the total number of bits in the collection
    total_bits = N * 1000
    
    # Calculate the maximum number of bits that can be used for compression
    max_bits = total_bits * b / 100
    
    # Check if the maximum number of bits is greater than or equal to the total number of bits
    if max_bits >= total_bits:
        return "yes"
    else:
        return "no"

