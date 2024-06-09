
def f1(player, n, cuboids):
    # Initialize the game state
    game_state = {}
    game_state["player"] = player
    game_state["n"] = n
    game_state["cuboids"] = cuboids
    game_state["turn"] = 0

    # Play the game
    while len(game_state["cuboids"]) > 0:
        # Get the current player
        current_player = game_state["player"]

        # Get the current cuboid
        current_cuboid = game_state["cuboids"][0]

        # Get the current move
        current_move = get_move(current_player, current_cuboid)

        # Apply the move
        new_cuboids = apply_move(current_cuboid, current_move)

        # Update the game state
        game_state["cuboids"] = new_cuboids
        game_state["turn"] += 1

    # Determine the winner
    winner = game_state["player"]

    return winner

def f2(player, n, cuboids):
    # Initialize the game state
    game_state = {}
    game_state["player"] = player
    game_state["n"] = n
    game_state["cuboids"] = cuboids
    game_state["turn"] = 0

    # Play the game
    while len(game_state["cuboids"]) > 0:
        # Get the current player
        current_player = game_state["player"]

        # Get the current cuboid
        current_cuboid = game_state["cuboids"][0]

        # Get the current move
        current_move = get_move(current_player, current_cuboid)

        # Apply the move
        new_cuboids = apply_move(current_cuboid, current_move)

        # Update the game state
        game_state["cuboids"] = new_cuboids
        game_state["turn"] += 1

    # Determine the winner
    winner = game_state["player"]

    return winner

def get_move(player, cuboid):
    # Initialize the move
    move = {}
    move["player"] = player
    move["cuboid"] = cuboid
    move["axes"] = []

    # Get the axes
    for i in range(3):
        axis = input("Enter axis {}: ".format(i + 1))
        move["axes"].append(axis)

    return move

def apply_move(cuboid, move):
    # Initialize the new cuboids
    new_cuboids = []

    # Get the axes
    axes = move["axes"]

    # Apply the move
    for i in range(3):
        axis = axes[i]
        if axis == 1:
            new_cuboids.append(cuboid)
        else:
            new_cuboids.append(cuboid[i])

    return new_cuboids

if __name__ == '__main__':
    player = input("Enter player: ")
    n = int(input("Enter number of cuboids: "))
    cuboids = []
    for i in range(n):
        x, y, z = map(int, input("Enter cuboid: ").split())
        cuboids.append((x, y, z))
    winner = f1(player, n, cuboids)
    print(winner)

