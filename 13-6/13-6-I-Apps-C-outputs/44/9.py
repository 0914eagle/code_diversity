
import math

def get_probability(m, n, t, p):
    # Calculate the probability that a single person wins the lottery
    prob_single_win = n / m

    # Calculate the probability that a person in the group wins the lottery
    prob_group_win = prob_single_win ** p

    # Calculate the probability that at least one person in the group wins the lottery
    prob_at_least_one_win = 1 - math.pow(1 - prob_single_win, p)

    # Calculate the probability that all people in the group win the lottery
    prob_all_win = prob_group_win * prob_at_least_one_win

    # Calculate the probability that the group can get tickets
    prob_tickets = prob_all_win * t

    return prob_tickets

