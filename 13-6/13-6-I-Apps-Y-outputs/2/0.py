
def refill_fridge(n, m, s, d, current_bottles):
    # Initialize the probability of all students getting a cold soda to 0
    prob_cold_soda = 0
    # Initialize the refill scheme with all 0s
    refill_scheme = [0] * s

    # Loop through each slot in the fridge
    for i in range(s):
        # Calculate the number of empty slots in the fridge
        empty_slots = s - sum(current_bottles)

        # Calculate the number of new bottles that can be placed in the current slot
        num_new_bottles = min(n, empty_slots)

        # Update the number of new bottles left to place
        n -= num_new_bottles

        # Update the number of empty slots in the fridge
        empty_slots -= num_new_bottles

        # Calculate the probability of all students getting a cold soda in the current slot
        prob_current_slot = (d - current_bottles[i]) / d

        # Update the probability of all students getting a cold soda
        prob_cold_soda += prob_current_slot ** m

        # Update the refill scheme
        refill_scheme[i] = num_new_bottles

    # Check if it is possible for all students to get a cold soda
    if prob_cold_soda == 1:
        return refill_scheme
    else:
        return "impossible"

