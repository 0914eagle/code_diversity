
def get_min_diff(n):
    # Calculate the sum of weights for each pile
    sum1 = sum([2**i for i in range(n//2)])
    sum2 = sum([2**i for i in range(n//2, n)])
    
    # Return the absolute difference between the two sums
    return abs(sum1 - sum2)

