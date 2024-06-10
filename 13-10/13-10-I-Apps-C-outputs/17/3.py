
def get_possible_moves(cards, k):
    # Initialize a list to store the possible moves
    possible_moves = []
    
    # Iterate over the cards
    for i in range(len(cards)):
        # Check if the current card is facing up
        if cards[i] == 1:
            # Check if the next k-1 cards are also facing up
            if all(cards[i+1:i+k]):
                # Add the current card and the next k-1 cards to the possible moves
                possible_moves.append([i, i+k-1])
    
    # Return the possible moves
    return possible_moves

def get_winner(cards, possible_moves):
    # Initialize a variable to store the winner
    winner = None
    
    # Iterate over the possible moves
    for move in possible_moves:
        # Check if the current move will result in a win
        if will_win(cards, move):
            # Set the winner to Tokitsukaze
            winner = "tokitsukaze"
            break
    
    # If the winner is still None, it means that Quailty can make a move that will result in a win
    if winner is None:
        winner = "quailty"
    
    # Return the winner
    return winner

def will_win(cards, move):
    # Initialize a variable to store the result
    result = False
    
    # Check if the current move will result in a win
    if all(cards[move[0]:move[1]+1]):
        result = True
    
    # Return the result
    return result

def main():
    # Read the input
    n, k = map(int, input().split())
    cards = list(map(int, input()))
    
    # Get the possible moves
    possible_moves = get_possible_moves(cards, k)
    
    # Get the winner
    winner = get_winner(cards, possible_moves)
    
    # Print the result
    if len(possible_moves) > 10**9:
        print("once again")
    else:
        print(winner)

if __name__ == '__main__':
    main()

