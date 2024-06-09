
import math

def solve(m, n, t, p):
    # Calculate the probability of each person winning the lottery
    prob = n / m

    # Calculate the number of people who can win the lottery
    num_winners = min(n, p)

    # Calculate the probability of the group winning the lottery
    group_prob = math.comb(n, num_winners) * prob ** num_winners * (1 - prob) ** (n - num_winners)

    # Calculate the probability of each person winning at least one ticket
    ticket_prob = group_prob * t / m

    # Calculate the probability of the group getting tickets
    return ticket_prob ** p

