
def refill_fridge(n, m, s, d, current_slots):
    # Initialize the probability of all students getting a cold soda as 0
    prob = 0

    # Initialize the refill scheme as an empty list
    refill_scheme = []

    # Loop through each slot in the fridge
    for i in range(s):
        # Calculate the number of empty slots in the current slot
        empty_slots = d - current_slots[i]

        # If the number of empty slots is greater than or equal to the number of new bottles,
        # then we can fill the empty slots with the new bottles and calculate the probability
        # of all students getting a cold soda
        if empty_slots >= n:
            # Calculate the number of cold sodas that will be available after the refill
            cold_sodas = current_slots[i] + n

            # Calculate the probability of all students getting a cold soda
            prob = cold_sodas / (cold_sodas + m * (d - cold_sodas))

            # If the probability is greater than or equal to 1, then we have found an optimal refill scheme
            if prob >= 1:
                # Fill the empty slots with the new bottles
                refill_scheme = [n] * i + [0] * (s - i)
                break

    # If no optimal refill scheme was found, return "impossible"
    if not refill_scheme:
        return "impossible"

    # Return the refill scheme
    return refill_scheme

