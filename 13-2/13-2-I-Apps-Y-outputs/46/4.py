
def reconstruct_winner(record):
    # Initialize the score for Alice and Barbara
    alice_score = 0
    barbara_score = 0
    
    # Iterate through the record
    for i in range(0, len(record), 2):
        # Get the current player and the number of points scored
        player = record[i]
        points = int(record[i+1])
        
        # Update the score for the current player
        if player == "A":
            alice_score += points
        else:
            barbara_score += points
        
        # Check if the game is over
        if alice_score >= 11 and barbara_score >= 11:
            # If the score is tied, the first player to lead by at least 2 points wins
            if alice_score == barbara_score:
                if alice_score - points >= barbara_score + 2:
                    return "A"
                else:
                    return "B"
            # Otherwise, the first player to 11 points wins
            else:
                return "A" if alice_score > barbara_score else "B"
    
    # If the game is not over, return "D" to indicate the game is still in progress
    return "D"

