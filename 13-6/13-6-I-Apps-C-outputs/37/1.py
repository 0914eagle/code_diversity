
def explosion(n, m, d, your_minions, opponent_minions):
    # Calculate the total number of minions
    total_minions = n + m
    
    # Calculate the probability of a minion surviving the explosion
    survival_probability = 1 - (d / total_minions)
    
    # Calculate the probability of all opponent's minions surviving the explosion
    opponent_survival_probability = survival_probability ** m
    
    # Calculate the probability of all your minions surviving the explosion
    your_survival_probability = survival_probability ** n
    
    # Calculate the probability of all opponent's minions being removed
    removal_probability = 1 - opponent_survival_probability
    
    # Return the probability of all opponent's minions being removed
    return removal_probability

