
def get_winner(s):
    if len(s) == 3:
        return "First"
    
    # Initialize the game state
    game_state = list(s)
    game_state.pop(0)
    game_state.pop(-1)
    
    # Determine which player will win
    if len(game_state) % 2 == 0:
        return "First"
    else:
        return "Second"

def main():
    s = input()
    print(get_winner(s))

if __name__ == '__main__':
    main()

