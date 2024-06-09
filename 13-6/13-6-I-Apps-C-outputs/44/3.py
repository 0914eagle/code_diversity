
import math

def get_probability(m, n, t, p):
    # Calculate the probability that a single person wins the lottery
    probability = n / m
    
    # Calculate the probability that p people win the lottery
    probability = probability ** p
    
    # Calculate the number of tickets that can be bought by p people
    tickets = t * p
    
    # Calculate the probability that p people can get tickets
    probability = probability * (tickets / m)
    
    return probability

