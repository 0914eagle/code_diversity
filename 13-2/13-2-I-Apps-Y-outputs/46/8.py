
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
        if alice_score >= 11 and alice_score - barbara_score >= 2:
            return "A"
        elif barbara_score >= 11 and barbara_score - alice_score >= 2:
            return "B"
    
    # If the game is not over, return "D"
    return "D"

