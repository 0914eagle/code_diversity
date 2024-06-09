
def refill_fridge(n, m, s, d, current_bottles):
    # Initialize the probability of all students getting a cold soda as 0
    prob = 0
    # Initialize the refill scheme as an empty list
    refill_scheme = []
    
    # Loop through each slot in the fridge
    for i in range(s):
        # Calculate the number of empty slots in the current slot
        empty_slots = d - current_bottles[i]
        # Calculate the number of new bottles that can be placed in the current slot
        num_new_bottles = min(empty_slots, n)
        # Add the number of new bottles to the refill scheme
        refill_scheme.extend([num_new_bottles] * num_new_bottles)
        # Subtract the number of new bottles from the total number of new bottles left to place
        n -= num_new_bottles
    
    # Calculate the probability of all students getting a cold soda
    prob = 1 - (n / (s * d)) ** m
    
    # If the probability is greater than 0, return the refill scheme
    if prob > 0:
        return refill_scheme
    # Otherwise, return "impossible"
    else:
        return "impossible"

