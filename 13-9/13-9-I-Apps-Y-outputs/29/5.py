
def refill_fridge(n, m, s, d, current_bottles):
    # Initialize the probability of all students getting a cold soda to 0
    prob_cold_soda = 0
    
    # Loop through all possible combinations of placing the new bottles in the fridge
    for combination in itertools.product(range(n+1), repeat=s):
        # Calculate the number of cold bottles in the fridge after this combination
        num_cold_bottles = sum(combination)
        
        # Calculate the probability of all students getting a cold soda after this combination
        prob_cold_soda_combination = math.comb(s, num_cold_bottles) * math.comb(n, num_cold_bottles) / math.comb(n+s, m)
        
        # If the probability of all students getting a cold soda after this combination is greater than the current maximum, update the maximum and the corresponding combination
        if prob_cold_soda_combination > prob_cold_soda:
            prob_cold_soda = prob_cold_soda_combination
            optimal_combination = combination
    
    # If the probability of all students getting a cold soda is 0, return "impossible"
    if prob_cold_soda == 0:
        return "impossible"
    
    # Otherwise, return the optimal combination of placing the new bottles in the fridge
    return list(optimal_combination)

