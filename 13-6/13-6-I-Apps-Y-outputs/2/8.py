
def refill_fridge(n, m, s, d, current_slots):
    # Initialize the probability of all students getting a cold soda to 0
    prob_cold_soda = 0

    # Loop through all possible ways to refill the fridge
    for i in range(n + 1):
        for j in range(n - i + 1):
            for k in range(n - i - j + 1):
                # Calculate the number of cold sodas in each slot
                num_cold_sodas = [current_slots[0] + i, current_slots[1] + j, current_slots[2] + k]

                # Calculate the probability of all students getting a cold soda
                prob_cold_soda_temp = 1
                for num_cold in num_cold_sodas:
                    prob_cold_soda_temp *= (num_cold / (i + j + k + num_cold)) ** m

                # If the probability is greater than the current probability, update the probability and the refill scheme
                if prob_cold_soda_temp > prob_cold_soda:
                    prob_cold_soda = prob_cold_soda_temp
                    refill_scheme = [i, j, k]

    # If the probability is 0, it is impossible for all students to get a cold soda, so return "impossible"
    if prob_cold_soda == 0:
        return "impossible"

    # Otherwise, return the refill scheme that maximizes the probability
    return refill_scheme

