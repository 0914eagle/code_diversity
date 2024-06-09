
import itertools
import math

def explosion_probability(n, m, d, my_minions, op_minions):
    # Calculate the total number of minions on the board
    total_minions = n + m
    
    # Calculate the probability of each minion receiving a unit of damage
    prob = 1 / total_minions
    
    # Calculate the number of units of damage that will be dealt
    num_units = min(d, total_minions)
    
    # Initialize the probability of removing all opponent's minions to 0
    probability = 0
    
    # Iterate over all possible combinations of minions receiving damage
    for combination in itertools.combinations(range(total_minions), num_units):
        # Calculate the probability of this specific combination of minions receiving damage
        combination_probability = prob ** len(combination) * (1 - prob) ** (total_minions - len(combination))
        
        # Calculate the number of opponent's minions that will be removed by this combination
        num_op_minions_removed = sum(1 for i in combination if i >= n)
        
        # Calculate the probability of removing all opponent's minions with this combination
        num_op_minions_remaining = m - num_op_minions_removed
        probability_all_op_minions_removed = num_op_minions_remaining == 0
        
        # Add the probability of this specific combination to the total probability
        probability += combination_probability * probability_all_op_minions_removed
    
    return probability

