
def get_min_weight_difference(n):
    # Calculate the sum of weights for each pile
    sum_first_pile = sum([2**i for i in range(n//2)])
    sum_second_pile = sum([2**i for i in range(n//2, n)])
    
    # Return the absolute difference between the two sums
    return abs(sum_first_pile - sum_second_pile)

