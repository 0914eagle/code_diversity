
def refill_fridge(n, m, s, d, current_bottles):
    # Initialize the probability of all students getting a cold soda to 0
    probability = 0

    # Loop through all possible ways to refill the fridge
    for refill_scheme in itertools.product(range(n + 1), repeat=s):
        # Calculate the number of cold sodas that will be in each slot after the refill
        new_bottles = [sum(refill_scheme[:i]) for i in range(1, s + 1)]

        # Calculate the probability that all students will get a cold soda
        probability = 1
        for i in range(s):
            probability *= binom.pmf(current_bottles[i], d, new_bottles[i] / (d + new_bottles[i]))

        # If the probability is greater than or equal to the previous maximum probability, save the refill scheme
        if probability >= max_probability:
            max_probability = probability
            optimal_scheme = refill_scheme

    # If the maximum probability is greater than 0, return the optimal refill scheme
    if max_probability > 0:
        return list(optimal_scheme)
    else:
        return "impossible"

