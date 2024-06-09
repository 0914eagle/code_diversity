
def get_balanced_sweets(m, k, a, b):
    # Calculate the target fractions
    f = [ai / sum(a) for ai in a]
    
    # Initialize the number of sweets to buy
    num_sweets = 0
    
    # Loop through each sweet type
    for i in range(m):
        # Calculate the current fraction of sweets of type i
        current_fraction = b.count(i + 1) / k
        
        # Calculate the difference between the current fraction and the target fraction
        diff = abs(current_fraction - f[i])
        
        # If the difference is greater than the number of sweets to buy, buy all the sweets of type i
        if diff > num_sweets:
            num_sweets = diff
    
    return num_sweets

