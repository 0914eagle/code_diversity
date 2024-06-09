
def refill_fridge(n, m, s, d, current_bottles):
    # Initialize the probability of all students getting a cold soda to 0
    prob_cold_soda = 0

    # Initialize the number of new bottles to be placed in each slot
    new_bottles = [0] * s

    # Loop through each slot
    for i in range(s):
        # Calculate the number of cold bottles in the current slot
        num_cold_bottles = current_bottles[i]

        # Calculate the number of new bottles that need to be placed in the current slot
        num_new_bottles = min(n, d - num_cold_bottles)

        # Update the number of new bottles to be placed in each slot
        new_bottles[i] += num_new_bottles
        n -= num_new_bottles

        # Calculate the probability of all students getting a cold soda from the current slot
        prob_cold_soda += num_cold_bottles / (num_cold_bottles + num_new_bottles)

    # Check if it is possible for all students to get a cold soda
    if prob_cold_soda < m:
        return "impossible"

    # Return the refill scheme that maximizes the probability of all students getting a cold soda
    return new_bottles

