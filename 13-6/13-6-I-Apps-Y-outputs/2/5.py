
def refill_fridge(n, m, s, d, current_bottles):
    # Initialize the probability of all students getting a cold soda as 0
    prob = 0
    # Initialize the refill scheme as an empty list
    refill_scheme = []
    
    # Loop through each slot in the fridge
    for i in range(s):
        # Calculate the number of empty slots in the current slot
        empty_slots = d - current_bottles[i]
        # If there are enough empty slots to fit all the new bottles, update the probability and refill scheme
        if empty_slots >= n:
            prob += 1 / (s * m)
            refill_scheme += [n]
            break
        # If there are not enough empty slots, update the probability and refill scheme
        else:
            prob += empty_slots / (s * m)
            refill_scheme += [empty_slots]
            n -= empty_slots
    
    # If the probability is greater than or equal to 1, return the refill scheme
    if prob >= 1:
        return refill_scheme
    # If the probability is less than 1, return "impossible"
    else:
        return "impossible"

