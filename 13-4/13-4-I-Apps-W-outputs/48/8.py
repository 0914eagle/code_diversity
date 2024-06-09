
def f1(player, n, cuboids):
    # Initialize the game state
    game_state = {
        "player": player,
        "cuboids": cuboids,
        "moves": []
    }

    # Play the game until a winner is determined
    while len(game_state["cuboids"]) > 1:
        # Get the current player and their move
        current_player = game_state["player"]
        current_move = get_move(current_player, game_state["cuboids"])

        # Update the game state with the current move
        game_state["moves"].append(current_move)
        game_state["cuboids"] = make_move(current_move, game_state["cuboids"])

        # Switch players
        game_state["player"] = "RUBEN" if current_player == "ALBERT" else "ALBERT"

    # Determine the winner and return their name
    return game_state["player"]

def get_move(player, cuboids):
    # Choose a cuboid to cut
    cuboid_to_cut = cuboids[0]

    # Choose the axes to cut along
    axes = [1, 1, 1]

    # Cut the cuboid and return the resulting smaller cuboids
    return [cuboid_to_cut[0] - axes[0], cuboid_to_cut[1] - axes[1], cuboid_to_cut[2] - axes[2]]

def make_move(move, cuboids):
    # Update the cuboids with the move
    return [cuboid - move for cuboid in cuboids]

if __name__ == '__main__':
    player = input()
    n = int(input())
    cuboids = []
    for _ in range(n):
        x, y, z = map(int, input().split())
        cuboids.append([x, y, z])
    print(f1(player, n, cuboids))

