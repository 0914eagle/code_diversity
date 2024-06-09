
import math

def lottery_probability(m, n, t, p):
    # Calculate the probability that a single person wins the lottery
    probability = n / m
    
    # Calculate the probability that p people win the lottery
    probability = probability ** p
    
    # Calculate the number of ways to choose t tickets for p people
    num_ways = math.comb(t, p)
    
    # Calculate the probability that p people can get tickets
    probability = probability * num_ways
    
    return probability

