
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
            if alice_score - barbara_score >= 2:
                return "A"
            else:
                return "B"
    
    # If the game is not over, return "D"
    return "D"

def main():
    record = input("Enter the record of the game: ")
    print(get_winner(record))

if __name__ == '__main__':
    main()

