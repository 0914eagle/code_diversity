
def solve(x, k):
    # Calculate the number of dresses after k months
    num_dresses = x
    for i in range(k):
        num_dresses *= 2
        num_dresses -= num_dresses // 2
    
    # Calculate the expected number of dresses
    expected = num_dresses / 2
    
    # Return the result modulo 10^9 + 7
    return expected % (10**9 + 7)

