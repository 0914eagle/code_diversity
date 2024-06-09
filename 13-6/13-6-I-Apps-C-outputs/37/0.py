
import itertools
import math

def explosion_probability(n, m, d, my_minions, opponent_minions):
    # Calculate the total number of minions left on the board after the explosion
    total_minions = n + m
    
    # Calculate the probability of each minion surviving the explosion
    probabilities = []
    for i in range(total_minions):
        probabilities.append(math.pow(1 - (i + 1) / total_minions, d))
    
    # Calculate the probability of all opponent's minions surviving the explosion
    opponent_survival_probability = 1
    for i in range(m):
        opponent_survival_probability -= probabilities[i]
    
    return opponent_survival_probability

# Test the function with the sample input
n = 1
m = 2
d = 2
my_minions = [2, 1]
opponent_minions = [1, 1]
print(explosion_probability(n, m, d, my_minions, opponent_minions))

