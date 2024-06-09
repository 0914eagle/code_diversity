
def explosion_probability(n, m, d, your_minions, opponent_minions):
    # Calculate the total number of minions
    total_minions = n + m
    
    # Calculate the probability of a minion surviving the explosion
    minion_survival_probability = 1 - (d / total_minions)
    
    # Calculate the probability of all opponent's minions surviving the explosion
    opponent_minions_survival_probability = 1
    for i in range(m):
        opponent_minions_survival_probability *= minion_survival_probability
    
    # Calculate the probability of all your minions surviving the explosion
    your_minions_survival_probability = 1
    for i in range(n):
        your_minions_survival_probability *= minion_survival_probability
    
    # Calculate the probability of all opponent's minions being removed
    probability = opponent_minions_survival_probability * your_minions_survival_probability
    
    return probability

