
def refill_fridge(n, m, s, d, current_bottles):
    # Initialize the probability of getting a cold soda as 0
    probability = 0
    # Initialize the refill scheme as an empty list
    refill_scheme = []
    
    # Loop through each slot in the fridge
    for i in range(s):
        # Check if the current slot has enough space for the new bottles
        if d - current_bottles[i] >= n:
            # If the slot has enough space, add the new bottles to the front of the slot
            refill_scheme.append(n)
            # Update the probability of getting a cold soda
            probability += (n / (d * m))
            # Break out of the loop since we have found an optimal refill scheme
            break
        # If the slot does not have enough space, try the next slot
        else:
            continue
    
    # If the probability of getting a cold soda is greater than or equal to 1, return the refill scheme
    if probability >= 1:
        return refill_scheme
    # If the probability of getting a cold soda is less than 1, return "impossible"
    else:
        return "impossible"

