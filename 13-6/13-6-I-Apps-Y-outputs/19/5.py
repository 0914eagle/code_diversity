
def get_winner(game_record):
    # Initialize the score for Alice and Barbara
    alice_score = 0
    barbara_score = 0
    
    # Iterate through the game record
    for i in range(0, len(game_record), 2):
        # Get the current player and the number of points scored
        current_player = game_record[i]
        points_scored = int(game_record[i+1])
        
        # Update the score for the current player
        if current_player == "A":
            alice_score += points_scored
        else:
            barbara_score += points_scored
        
        # Check if the game is over
        if alice_score >= 11 and barbara_score >= 11:
            # If the score is tied, check if the game is won by 2
            if alice_score - barbara_score >= 2:
                return "A"
            elif barbara_score - alice_score >= 2:
                return "B"
    
    # If the game is not over, return None
    return None

def main():
    game_record = input("Enter the game record: ")
    winner = get_winner(game_record)
    if winner:
        print(f"The winner is {winner}")
    else:
        print("The game is not over yet.")

if __name__ == '__main__':
    main()

