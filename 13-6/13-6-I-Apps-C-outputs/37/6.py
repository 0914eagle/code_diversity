
import itertools
import math

def explosion_probability(n, m, d, your_minions, opponent_minions):
    # Calculate the total health of both players
    total_health = sum(your_minions) + sum(opponent_minions)
    
    # Calculate the probability of each minion surviving the explosion
    probabilities = []
    for i in range(d):
        # Calculate the probability of each minion surviving this turn
        prob = 0
        for j in range(n):
            prob += (your_minions[j] - i) / total_health
        for j in range(m):
            prob += (opponent_minions[j] - i) / total_health
        
        # Add the probability to the list
        probabilities.append(prob)
    
    # Calculate the probability that all opponent minions are removed
    probability = 1
    for i in range(d):
        probability *= probabilities[i]
    
    return probability

