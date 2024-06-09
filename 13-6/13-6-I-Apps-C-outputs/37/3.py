
def explosion(n, m, d, my_minions, opp_minions):
    # Calculate the total health of both players
    total_health = sum(my_minions) + sum(opp_minions)

    # Calculate the probability of each minion being hit
    prob = d / total_health

    # Calculate the probability of all opponent's minions being hit
    opp_prob = prob ** m

    # Calculate the probability of all my minions being hit
    my_prob = prob ** n

    # Calculate the probability of all opponent's minions being hit and all my minions being hit
    both_prob = opp_prob * my_prob

    # Return the probability of all opponent's minions being hit
    return 1 - both_prob

