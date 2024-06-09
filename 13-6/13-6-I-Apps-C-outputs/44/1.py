
import math

def get_probability(m, n, t, p):
    # Calculate the probability that a single person wins the lottery
    prob_win = n / m
    
    # Calculate the probability that a person wins the lottery and buys all p tickets
    prob_win_all = prob_win * (t ** p)
    
    # Calculate the probability that a person wins the lottery and buys at least one ticket
    prob_win_at_least_one = prob_win * (t ** (p - 1)) * (1 - (t - 1) / t)
    
    # Calculate the probability that your group wins the lottery and gets all p tickets
    prob_group_wins = prob_win_all * (p / m)
    
    # Calculate the probability that your group wins the lottery and gets at least one ticket
    prob_group_wins_at_least_one = prob_win_at_least_one * (p / m)
    
    # Return the probability that your group gets tickets to the show
    return prob_group_wins + prob_group_wins_at_least_one

