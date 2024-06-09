
def refill_fridge(n, m, s, d, current_slots):
    # Initialize the probability of all students getting a cold soda as 0
    probability = 0
    # Initialize the refill scheme as an empty list
    refill_scheme = []
    
    # Loop through each slot in the fridge
    for i in range(s):
        # Calculate the number of empty slots in front of the current slot
        empty_slots = s - i - 1
        # Calculate the number of new bottles that can be placed in front of the current slot
        num_bottles = min(n, empty_slots)
        # Calculate the probability of all students getting a cold soda if the new bottles are placed in front of the current slot
        prob = calculate_probability(num_bottles, m, d, current_slots[i])
        # If the probability is higher than the current probability, update the probability and the refill scheme
        if prob > probability:
            probability = prob
            refill_scheme = [num_bottles] * i + [0] * (s - i)
    
    # If the probability is 0, it is impossible for all students to get a cold soda, so return "impossible"
    if probability == 0:
        return "impossible"
    # Otherwise, return the refill scheme that maximizes the probability of all students getting a cold soda
    return refill_scheme

def calculate_probability(num_bottles, m, d, current_slot):
    # Calculate the probability of all students getting a cold soda if the new bottles are placed in front of the current slot
    probability = 1
    for i in range(m):
        # Calculate the probability of the current student getting a cold soda
        prob = (current_slot + num_bottles - i) / (d + num_bottles)
        # Multiply the probability by the probability of the next student getting a cold soda
        probability *= prob
    
    return probability

