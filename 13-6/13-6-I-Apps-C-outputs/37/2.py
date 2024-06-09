
import itertools
import math

def explosion_probability(n, m, d, my_minions, opp_minions):
    # Calculate the total number of combinations of minions that can be affected by the explosion
    total_combinations = math.comb(n + m, d)

    # Initialize a list to store the probabilities for each combination
    probabilities = [0] * total_combinations

    # Iterate over all possible combinations of minions that can be affected by the explosion
    for i, combination in enumerate(itertools.combinations(range(n + m), d)):
        # Initialize the probability for this combination to 1
        probability = 1

        # Iterate over the minions in the combination
        for minion in combination:
            # If the minion is an opponent's minion, calculate the probability that it will be removed
            if minion >= n:
                probability *= (opp_minions[minion - n] - 1) / 6
            # If the minion is one of your own minions, calculate the probability that it will be removed
            else:
                probability *= (my_minions[minion] - 1) / 6

        # Add the probability for this combination to the list of probabilities
        probabilities[i] = probability

    # Return the sum of the probabilities for all combinations
    return sum(probabilities)

