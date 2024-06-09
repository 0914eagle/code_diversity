
def refill_fridge(n, m, s, d, current_slots):
    # Initialize the probability of all students getting a cold soda as 0
    prob_cold_soda = 0
    # Initialize the number of new bottles to be placed in each slot as 0
    new_bottles = [0] * s
    # Loop through each slot
    for i in range(s):
        # Calculate the number of cold bottles in the current slot
        num_cold_bottles = current_slots[i]
        # Calculate the number of new bottles that can be placed in the current slot
        num_new_bottles = min(n, d - num_cold_bottles)
        # Update the number of new bottles to be placed in the current slot
        new_bottles[i] = num_new_bottles
        # Update the number of new bottles left to be placed
        n -= num_new_bottles
        # Calculate the probability of all students getting a cold soda from the current slot
        prob_cold_soda += num_cold_bottles / (num_cold_bottles + num_new_bottles)
        # If the probability of all students getting a cold soda from the current slot is 1, break the loop
        if prob_cold_soda == 1:
            break
    # If the probability of all students getting a cold soda is 1, return the number of new bottles to be placed in each slot
    if prob_cold_soda == 1:
        return new_bottles
    # Otherwise, return "impossible"
    else:
        return "impossible"

