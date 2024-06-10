
def determine_winner(s):
    if len(s) == 3:
        return "First"
    
    # Initialize the game state
    game_state = s
    player = "Takahashi"
    
    while True:
        # Determine the next move
        next_move = determine_next_move(game_state, player)
        if next_move == None:
            break
        game_state = next_move
        player = "Aoki" if player == "Takahashi" else "Takahashi"
    
    # Determine the winner
    if player == "Takahashi":
        return "First"
    else:
        return "Second"

def determine_next_move(game_state, player):
    # Determine the available moves
    available_moves = []
    for i in range(len(game_state)):
        if game_state[i] != game_state[i-1] and game_state[i] != game_state[i+1]:
            available_moves.append(i)
    
    # If there are no available moves, the game is over
    if len(available_moves) == 0:
        return None
    
    # Determine the next move
    if player == "Takahashi":
        return game_state[:available_moves[0]] + game_state[available_moves[0]+1:]
    else:
        return game_state[:available_moves[-1]] + game_state[available_moves[-1]+1:]

if __name__ == '__main__':
    s = input()
    print(determine_winner(s))

