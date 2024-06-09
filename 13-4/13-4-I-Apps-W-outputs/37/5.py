
def solve(player, n, cuboids):
    # Initialize the game state
    game_state = {
        "player": player,
        "cuboids": cuboids,
        "moves": []
    }

    # While there are still cuboids left in the game
    while len(game_state["cuboids"]) > 0:
        # Get the current player and their move
        current_player = game_state["player"]
        current_move = get_move(game_state)

        # Update the game state with the current move
        game_state = update_game_state(game_state, current_move)

        # Switch to the other player's turn
        game_state["player"] = "RUBEN" if current_player == "ALBERT" else "ALBERT"

    # Return the winner of the game
    return game_state["player"]

def get_move(game_state):
    # TODO: Implement this function to return the current player's move
    pass

def update_game_state(game_state, move):
    # TODO: Implement this function to update the game state with the current move
    pass

player = input()
n = int(input())
cuboids = []

for i in range(n):
    x, y, z = map(int, input().split())
    cuboids.append((x, y, z))

print(solve(player, n, cuboids))

