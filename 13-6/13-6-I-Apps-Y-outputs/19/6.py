
def get_winner(record):
    # Initialize the score of Alice and Barbara
    alice_score = 0
    barbara_score = 0
    
    # Iterate through the record
    for i in range(0, len(record), 2):
        # Get the score of the current player
        score = int(record[i+1])
        
        # Check if the current player is Alice
        if record[i] == "A":
            alice_score += score
        else:
            barbara_score += score
        
        # Check if the game is over
        if alice_score >= 11 and barbara_score >= 11:
            # Check if the score is tied
            if alice_score == barbara_score:
                # Check if the lead is at least 2
                if alice_score - barbara_score >= 2:
                    return "A"
                else:
                    return "B"
            else:
                # Return the player with the higher score
                if alice_score > barbara_score:
                    return "A"
                else:
                    return "B"
    
    # If the game is not over, return None
    return None

def main():
    record = input("Enter the record of the game: ")
    print(get_winner(record))

if __name__ == '__main__':
    main()

