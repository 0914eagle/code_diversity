
def solve(n, m):
    total_cards = n * m
    success_cases = 0

    # Loop through all possible cases
    for i in range(total_cards):
        # Calculate the probability of Alex successfully performing the trick
        success_probability = 1 / total_cards

        # Add the probability to the total success cases
        success_cases += success_probability

    # Return the probability of the trick being successful
    return success_cases

