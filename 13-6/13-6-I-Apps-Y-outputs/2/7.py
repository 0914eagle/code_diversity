
def get_refill_scheme(n, m, s, d, current_slots):
    # Initialize the probability of all students getting a cold soda to 0
    prob_cold_soda = 0
    # Initialize the refill scheme with the number of new bottles in each slot
    refill_scheme = [0] * s

    # Loop through each possible refill scheme
    for i in range(s):
        # Calculate the probability of all students getting a cold soda with this refill scheme
        prob_cold_soda_i = 1
        for j in range(m):
            # Calculate the probability of the jth student getting a cold soda with this refill scheme
            prob_cold_soda_j = 1
            for k in range(i):
                # Calculate the probability of the jth student getting a cold soda from slot k
                prob_cold_soda_j *= (d - current_slots[k]) / d
            prob_cold_soda_i *= prob_cold_soda_j
        prob_cold_soda_i **= (1 / m)
        prob_cold_soda += prob_cold_soda_i
        refill_scheme[i] = n

    # Find the maximum probability of all students getting a cold soda
    prob_cold_soda = max(prob_cold_soda, 0)

    # If the maximum probability is 0, then it is impossible for all students to get a cold soda
    if prob_cold_soda == 0:
        return "impossible"

    # Otherwise, return the refill scheme with the maximum probability
    return refill_scheme

