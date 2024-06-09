
def get_min_banknotes(n):
    # Initialize the minimum number of banknotes to infinity
    min_banknotes = float('inf')
    
    # Iterate through all possible values of banknotes from 1 to 10^100
    for i in range(1, 10**100+1):
        # Calculate the number of banknotes needed for the payment
        num_banknotes = n // i + (n % i > 0)
        
        # Update the minimum number of banknotes if necessary
        if num_banknotes < min_banknotes:
            min_banknotes = num_banknotes
    
    return min_banknotes

