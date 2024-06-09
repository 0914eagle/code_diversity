
def solve(k, n, questions):
    # Initialize the player with the box and the time elapsed
    player = k
    time_elapsed = 0
    
    # Iterate through the questions
    for i in range(n):
        # Unpack the question data
        time, answer = questions[i]
        
        # Update the time elapsed
        time_elapsed += time
        
        # If the answer is incorrect or skipped, pass the box to the next player
        if answer in ["N", "P"]:
            player = (player + 1) % 8
        
        # If the answer is correct, pass the box to the next player and update the time elapsed
        else:
            player = (player + 1) % 8
            time_elapsed += 30
    
    # Return the player with the box when it exploded
    return player

