
def refill_fridge(n, m, s, d, current_bottles):
    # Initialize the probability of all students getting a cold soda to 0
    prob_cold_soda = 0

    # Initialize the number of new bottles to add to each slot
    new_bottles = [0] * s

    # Loop through each slot
    for i in range(s):
        # Calculate the number of cold bottles in the current slot
        num_cold_bottles = current_bottles[i]

        # Calculate the number of new bottles needed to add to the slot
        num_new_bottles = max(0, n - num_cold_bottles)

        # Add the new bottles to the slot
        new_bottles[i] = num_new_bottles

        # Calculate the probability of all students getting a cold soda from the slot
        prob_cold_soda += (num_cold_bottles / d) ** m

    # If the probability of all students getting a cold soda is greater than 0, return the refill scheme
    if prob_cold_soda > 0:
        return new_bottles

    # Otherwise, return "impossible"
    return "impossible"

