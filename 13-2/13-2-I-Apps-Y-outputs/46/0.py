
def reconstruct_winner(record):
    # Initialize the score and the lead
    score = [0, 0]
    lead = 0
    
    # Iterate through the record
    for i in range(0, len(record), 2):
        # Get the current player and the number of points scored
        player = record[i]
        points = int(record[i+1])
        
        # Update the score and the lead
        score[player == "A"] += points
        lead = score[0] - score[1]
        
        # Check if the game is over
        if abs(lead) >= 2:
            break
    
    # Return the winner
    return "A" if lead > 0 else "B"

