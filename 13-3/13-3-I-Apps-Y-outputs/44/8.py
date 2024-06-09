
def solve(a1, b1, a2, b2):
    # Calculate the number of possible outcomes for each player
    num_outcomes_gunnar = (b1 - a1 + 1) * (b1 - a1 + 2) // 2
    num_outcomes_emma = (b2 - a2 + 1) * (b2 - a2 + 2) // 2
    
    # Calculate the probability of Gunnar winning
    prob_gunnar = num_outcomes_gunnar / (num_outcomes_gunnar + num_outcomes_emma)
    
    # Calculate the probability of Emma winning
    prob_emma = 1 - prob_gunnar
    
    # Check if the probability of both players is the same
    if prob_gunnar == prob_emma:
        return "Tie"
    # Return the name of the player with higher probability of winning
    elif prob_gunnar > prob_emma:
        return "Gunnar"
    else:
        return "Emma"

