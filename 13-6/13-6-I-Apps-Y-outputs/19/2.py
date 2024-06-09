
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
            # If the score is tied, the first player to lead by at least 2 points wins
            if alice_score - barbara_score >= 2:
                return "A"
            elif barbara_score - alice_score >= 2:
                return "B"
        elif alice_score >= 11:
            # Alice has won the game
            return "A"
        elif barbara_score >= 11:
            # Barbara has won the game
            return "B"
    
    # The game is still ongoing
    return "D"

def main():
    record = input()
    print(get_winner(record))

if __name__ == '__main__':
    main()

