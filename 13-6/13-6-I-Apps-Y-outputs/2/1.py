
def refill_fridge(n, m, s, d, current_slots):
    # Initialize the probability of all students getting a cold soda as 0
    prob_cold_soda = 0
    # Initialize the refill scheme as an empty list
    refill_scheme = []
    
    # Loop through each slot in the fridge
    for i in range(s):
        # Calculate the number of empty slots in front of the current slot
        empty_slots = s - i - 1
        # Calculate the number of new bottles that can be placed in front of the current slot
        num_new_bottles = min(n, empty_slots)
        # Calculate the number of cold bottles that can be placed in front of the current slot
        num_cold_bottles = min(current_slots[i], num_new_bottles)
        # Calculate the probability of all students getting a cold soda from the current slot
        prob_cold_soda += num_cold_bottles / (num_cold_bottles + num_new_bottles)
    
    # If the probability of all students getting a cold soda is greater than or equal to the number of students, return the refill scheme
    if prob_cold_soda >= m:
        return refill_scheme
    # Otherwise, return "impossible"
    else:
        return "impossible"

