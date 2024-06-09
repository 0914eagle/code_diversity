
def solve(a1, b1, a2, b2):
    # Calculate the number of possible outcomes for each die
    num_outcomes_die1 = b1 - a1 + 1
    num_outcomes_die2 = b2 - a2 + 1
    
    # Calculate the number of possible outcomes for each player
    num_outcomes_player1 = num_outcomes_die1 * num_outcomes_die2
    num_outcomes_player2 = num_outcomes_die1 * num_outcomes_die2
    
    # Check if one player has a higher probability of winning
    if num_outcomes_player1 > num_outcomes_player2:
        return "Gunnar"
    elif num_outcomes_player1 < num_outcomes_player2:
        return "Emma"
    else:
        return "Tie"

