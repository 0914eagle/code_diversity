
def explosion_probability(n, m, d, my_minions, opp_minions):
    # Calculate the total health of both players
    total_health = sum(my_minions) + sum(opp_minions)

    # Initialize the probability to 0
    probability = 0

    # Loop through all possible combinations of minions that could be removed
    for i in range(1, total_health + 1):
        # Calculate the probability of removing i minions
        prob = combination_probability(total_health, i)

        # Calculate the number of minions that would be left after removing i minions
        num_left = total_health - i

        # If all opponent's minions are removed, add the probability to the total probability
        if num_left == 0:
            probability += prob

        # If not all opponent's minions are removed, calculate the probability of removing all opponent's minions given that i minions are removed
        else:
            # Calculate the probability of removing all opponent's minions given that i minions are removed
            prob_opp = combination_probability(num_left, m)

            # Add the probability of removing all opponent's minions given that i minions are removed to the total probability
            probability += prob * prob_opp

    # Return the total probability
    return probability

# Calculate the probability of removing r minions from n minions
def combination_probability(n, r):
    # Calculate the binomial coefficient
    coefficient = binomial_coefficient(n, r)

    # Calculate the probability
    probability = coefficient * (0.5 ** r) * (0.5 ** (n - r))

    # Return the probability
    return probability

# Calculate the binomial coefficient
def binomial_coefficient(n, r):
    # Base case: n = r
    if n == r:
        return 1

    # Recursive case: n > r
    else:
        return (n * binomial_coefficient(n - 1, r)) // r

