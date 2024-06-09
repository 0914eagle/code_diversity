
def solve(N, b):
    # Calculate the total number of bits in the collection
    total_bits = N * 1000
    
    # Check if the total number of bits is less than or equal to b^N
    if total_bits <= b**N:
        return "yes"
    else:
        return "no"

