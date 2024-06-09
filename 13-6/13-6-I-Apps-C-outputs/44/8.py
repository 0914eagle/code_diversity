
import math

def get_probability(m, n, t, p):
    # Calculate the probability that a single person wins the lottery
    probability = n / m
    
    # Calculate the probability that p people win the lottery
    probability = probability ** p
    
    # Calculate the probability that at least one person in the group wins the lottery
    probability = 1 - (1 - probability) ** m
    
    return probability

