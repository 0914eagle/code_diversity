
import math

def lottery(m, n, t, p):
    # Calculate the probability of each person winning the lottery
    prob_win = n / m

    # Calculate the probability of each person winning the lottery and buying up to t tickets
    prob_win_t = prob_win * (t / m)

    # Calculate the probability that at least one person in the group wins the lottery
    prob_group_win = 1 - math.comb(m - 1, p - 1) * math.pow(1 - prob_win, p)

    # Calculate the probability that the group can get tickets
    prob_tickets = prob_group_win * prob_win_t ** p

    return prob_tickets

