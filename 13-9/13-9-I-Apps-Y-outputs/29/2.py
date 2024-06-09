
import random

def get_refill_scheme(n, m, s, d, current_slots):
    # Calculate the number of cold sodas in each slot
    num_cold_sodas = [current_slots[i] for i in range(s)]
    
    # Calculate the number of new sodas to add to each slot
    num_new_sodas = [min(n, d - num_cold_sodas[i]) for i in range(s)]
    
    # Add the new sodas to the front of each slot
    refill_scheme = [num_new_sodas[i] for i in range(s)]
    
    # Check if all the next m students will get a cold soda
    if sum(num_cold_sodas) + sum(num_new_sodas) >= m:
        return refill_scheme
    else:
        return "impossible"

