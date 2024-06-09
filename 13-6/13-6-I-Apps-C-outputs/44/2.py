
import math

def get_probability(m, n, t, p):
    # Calculate the probability that a single person wins the lottery
    probability = n / m
    
    # Calculate the number of people who can win the lottery
    num_winners = min(n, p)
    
    # Calculate the number of tickets each winner can buy
    num_tickets = min(t, p)
    
    # Calculate the probability that the group can get tickets
    probability = math.pow(probability, num_winners) * math.pow((1 - probability), (p - num_winners))
    
    return probability

