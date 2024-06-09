
def get_winner(record):
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
            # If the score is tied at 10-10, the game continues until one player leads by at least two points
            if alice_score == 11 and barbara_score == 11:
                continue
            else:
                # The first player to score 11 points wins
                break
    
    # Return the winner
    if alice_score > barbara_score:
        return "A"
    else:
        return "B"

def main():
    record = input("Enter the record of the game: ")
    winner = get_winner(record)
    print(f"The winner is {winner}")

if __name__ == '__main__':
    main()

