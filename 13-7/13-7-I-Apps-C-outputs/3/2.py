
def solve(s):
    if len(s) == 3:
        return "First"
    
    # Initialize the game state
    game_state = list(s)
    player = "Takahashi"
    
    while True:
        # Get the next player
        if player == "Takahashi":
            player = "Aoki"
        else:
            player = "Takahashi"
        
        # Get the next move
        if player == "Takahashi":
            # Takahashi removes the first character
            game_state = game_state[1:]
        else:
            # Aoki removes the last character
            game_state = game_state[:-1]
        
        # Check if the game has ended
        if len(game_state) == 3:
            return "First"
        if len(game_state) == 2:
            return "Second"
        
        # Check if the game is still ongoing
        if game_state[0] == game_state[1]:
            return "Second"
        if game_state[-1] == game_state[-2]:
            return "Second"
        
        # If the game is still ongoing, continue
        continue

def main():
    s = input()
    print(solve(s))

if __name__ == '__main__':
    main()

