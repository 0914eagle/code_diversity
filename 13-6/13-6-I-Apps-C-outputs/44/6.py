
import math

def get_probability(m, n, t, p):
    # Calculate the probability that a single person wins the lottery
    probability = n / m
    
    # Calculate the number of people who can win the lottery
    num_winners = min(n, p)
    
    # Calculate the probability that all people in the group win the lottery
    probability_all_win = math.comb(n, num_winners) * probability ** num_winners * (1 - probability) ** (n - num_winners)
    
    # Calculate the probability that at least one person in the group wins the lottery
    probability_at_least_one_win = 1 - math.comb(n, 0) * probability ** 0 * (1 - probability) ** n
    
    # Calculate the final probability
    probability = probability_all_win + probability_at_least_one_win
    
    return probability

