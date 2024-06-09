
def get_refill_scheme(n, m, s, d, current_slots):
    # Initialize the probability of getting a cold soda as 0
    prob_cold = 0
    # Initialize the refill scheme as an empty list
    refill_scheme = []

    # Loop through each slot in the fridge
    for i in range(s):
        # Calculate the number of empty slots in the fridge
        num_empty_slots = s - sum(current_slots)
        # Calculate the number of new bottles that can be placed in the current slot
        num_new_bottles = min(n, num_empty_slots)
        # Calculate the probability of getting a cold soda from the current slot
        prob_cold_current_slot = num_new_bottles / (num_new_bottles + current_slots[i])
        # Calculate the total probability of getting a cold soda from all the slots
        total_prob_cold = prob_cold + prob_cold_current_slot
        # If the total probability of getting a cold soda is greater than or equal to 1, return the refill scheme
        if total_prob_cold >= 1:
            return refill_scheme
        # If the total probability of getting a cold soda is less than 1, continue to the next slot
        else:
            # Add the number of new bottles to the refill scheme
            refill_scheme.append(num_new_bottles)
            # Subtract the number of new bottles from the number of new bottles remaining
            n -= num_new_bottles
            # Add the number of new bottles to the current slot
            current_slots[i] += num_new_bottles

    # If all the slots have been checked and a refill scheme has not been returned, return "impossible"
    return "impossible"

