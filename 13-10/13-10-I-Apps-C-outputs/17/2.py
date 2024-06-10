
def play_game(n, k, cards):
    # Initialize the game state
    game_state = cards
    # Initialize the number of moves
    num_moves = 0
    # Loop until the game ends
    while True:
        # Check if the game has ended
        if check_game_over(game_state):
            # If Tokitsukaze will win, return "tokitsukaze"
            if game_state.count("1") > game_state.count("0"):
                return "tokitsukaze"
            # If Quailty will win, return "quailty"
            elif game_state.count("1") < game_state.count("0"):
                return "quailty"
            # If the game ends in a draw, return "once again"
            else:
                return "once again"
        # Tokitsukaze's turn
        game_state = flip_cards(game_state, k)
        num_moves += 1
        # Check if the number of moves exceeds 10^9
        if num_moves > 10**9:
            return "once again"
        # Quailty's turn
        game_state = flip_cards(game_state, k)
        num_moves += 1
        # Check if the number of moves exceeds 10^9
        if num_moves > 10**9:
            return "once again"

def check_game_over(game_state):
    # Check if all the cards have the same color side facing up
    if game_state.count("1") == len(game_state):
        return True
    # Check if all the cards have the same color side facing down
    elif game_state.count("0") == len(game_state):
        return True
    # If the game is not over, return False
    else:
        return False

def flip_cards(game_state, k):
    # Initialize the flipped cards
    flipped_cards = ""
    # Loop through the game state
    for i in range(len(game_state)):
        # If the current card has not been flipped, flip it
        if game_state[i] == "0" or game_state[i] == "1":
            flipped_cards += "1" if game_state[i] == "0" else "0"
        # If the current card has already been flipped, keep it as it is
        else:
            flipped_cards += game_state[i]
    # Return the flipped cards
    return flipped_cards

if __name__ == '__main__':
    n, k = map(int, input().split())
    cards = input()
    print(play_game(n, k, cards))

