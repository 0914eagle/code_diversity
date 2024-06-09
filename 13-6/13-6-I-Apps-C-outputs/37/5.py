
import itertools
import math

def explosion_probability(n, m, d, your_minions, opponent_minions):
    # Calculate the total health of both players
    total_health = sum(your_minions) + sum(opponent_minions)
    
    # Calculate the probability of each minion being removed
    probabilities = []
    for i in range(m):
        # Calculate the probability of the i-th minion being removed
        probability = 0
        for j in range(d):
            # Calculate the probability of the j-th unit of damage being dealt to the i-th minion
            probability += (1 / total_health) * (1 / m)
        probabilities.append(probability)
    
    # Calculate the probability that all minions are removed
    probability = 1
    for i in range(m):
        probability *= 1 - probabilities[i]
    
    return probability

