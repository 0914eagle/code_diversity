
def get_winner(record):
    # Initialize the score of Alice and Barbara
    alice_score = 0
    barbara_score = 0
    
    # Iterate through the record
    for i in range(0, len(record), 2):
        # Get the current player and the number of points scored
        current_player = record[i]
        points_scored = int(record[i+1])
        
        # Update the score of the current player
        if current_player == "A":
            alice_score += points_scored
        else:
            barbara_score += points_scored
        
        # Check if the game is over
        if alice_score >= 11 and barbara_score >= 11:
            # If the score is tied, the first player to lead by at least 2 points wins
            if alice_score - barbara_score >= 2:
                return "A"
            elif barbara_score - alice_score >= 2:
                return "B"
        elif alice_score >= 11:
            # Alice wins if she reaches 11 points first
            return "A"
        elif barbara_score >= 11:
            # Barbara wins if she reaches 11 points first
            return "B"
    
    # If the game is not over, return "D" for draw
    return "D"

def main():
    record = input("Enter the game record: ")
    print(get_winner(record))

if __name__ == '__main__':
    main()

