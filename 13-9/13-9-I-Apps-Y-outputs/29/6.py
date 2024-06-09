
def refill_fridge(n, m, s, d, current_contents):
    # Initialize the probability of all students getting a cold soda to 0
    prob_all_cold = 0
    # Initialize the maximum probability of all students getting a cold soda
    max_prob_all_cold = 0
    # Initialize the refill scheme with the maximum probability of all students getting a cold soda
    optimal_refill_scheme = []

    # Iterate over all possible refill schemes
    for i in range(n + 1):
        for j in range(n - i + 1):
            for k in range(n - i - j + 1):
                # Calculate the number of cold sodas in the fridge after the refill scheme
                num_cold_sodas = sum(current_contents) + i
                # Calculate the probability of all students getting a cold soda
                prob_all_cold = (num_cold_sodas / (s * d)) ** m
                # If the probability is greater than the maximum probability, update the maximum probability and the optimal refill scheme
                if prob_all_cold > max_prob_all_cold:
                    max_prob_all_cold = prob_all_cold
                    optimal_refill_scheme = [i, j, k]

    # If the maximum probability is 0, it is impossible for all students to get a cold soda, so return "impossible"
    if max_prob_all_cold == 0:
        return "impossible"
    # Otherwise, return the optimal refill scheme
    else:
        return optimal_refill_scheme

