
def refill_fridge(n, m, s, d, current_slots):
    # Initialize the probability of all students getting a cold soda to 0
    probability = 0

    # Initialize the refill scheme with all 0s
    refill_scheme = [0] * s

    # Loop through all possible refill schemes
    for i in range(s):
        # Calculate the number of new bottles that can be placed in the front of slot i
        num_new_bottles = min(n, d - current_slots[i])

        # Calculate the number of cold bottles that will be left in the fridge after placing the new bottles in the front of slot i
        num_cold_bottles = current_slots[i] + num_new_bottles

        # Calculate the probability of all students getting a cold soda with this refill scheme
        probability_i = 1 - (num_cold_bottles / (d * m))

        # If the probability is greater than the current probability, update the refill scheme and probability
        if probability_i > probability:
            probability = probability_i
            refill_scheme = [num_new_bottles if i == j else 0 for j in range(s)]

    # If the probability is 0, it is impossible for all students to get a cold soda, so return "impossible"
    if probability == 0:
        return "impossible"

    # Otherwise, return the refill scheme that maximizes the probability
    return refill_scheme

