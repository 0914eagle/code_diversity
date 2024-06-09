
def get_winner(record):
    # Initialize the score for Alice and Barbara
    alice_score = 0
    barbara_score = 0
    
    # Iterate through the record
    for i in range(0, len(record), 2):
        # Get the current score and the number of points scored
        current_score = int(record[i+1])
        points_scored = int(record[i])
        
        # Update the score for the current player
        if record[i] == "A":
            alice_score += points_scored
        else:
            barbara_score += points_scored
        
        # Check if the game is over
        if alice_score >= 11 and barbara_score >= 11:
            # If the score is tied, check if the difference is at least 2
            if alice_score == barbara_score:
                if alice_score - barbara_score >= 2:
                    return "A"
                else:
                    return "B"
            # If Alice has more than 10 points, she wins
            else:
                return "A"
    
    # If the game is still going on, return None
    return None

def main():
    record = input("Enter the game record: ")
    winner = get_winner(record)
    if winner:
        print(f"The winner is {winner}")
    else:
        print("The game is still going on")

if __name__ == '__main__':
    main()

