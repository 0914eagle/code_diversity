
import math

def lottery_probability(m, n, t, p):
    # Calculate the probability of each person winning
    probability = n / m
    
    # Calculate the number of people who can win
    num_winners = min(n, p)
    
    # Calculate the number of tickets each winner can buy
    num_tickets = t * num_winners
    
    # Calculate the total number of tickets available
    total_tickets = m * t
    
    # Calculate the probability that your group can get tickets
    group_probability = math.comb(total_tickets, num_tickets) * probability ** num_winners * (1 - probability) ** (total_tickets - num_tickets)
    
    return group_probability

