
import itertools
import math

def explosion_probability(n, m, d, my_minions, opp_minions):
    # Calculate the total number of possible outcomes
    total_outcomes = math.factorial(n + m)
    
    # Calculate the number of outcomes where all opponent's minions are removed
    num_outcomes = 0
    for perm in itertools.permutations(range(n + m)):
        # Initialize the health of all minions
        minions = [0] * (n + m)
        for i in range(n):
            minions[i] = my_minions[i]
        for i in range(n, n + m):
            minions[i] = opp_minions[i - n]
        
        # Simulate the explosion
        for i in range(d):
            # Find the index of the minion to receive the damage
            idx = perm[i]
            if minions[idx] > 0:
                minions[idx] -= 1
            if minions[idx] == 0:
                # Remove the minion from the game
                minions[idx] = -1
        
        # Check if all opponent's minions are removed
        if all(minions[n:] == 0):
            num_outcomes += 1
    
    # Calculate the probability
    probability = num_outcomes / total_outcomes
    
    return probability

