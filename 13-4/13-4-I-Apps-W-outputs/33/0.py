
def get_minimum_bombs(n):
    # Initialize a list to store the positions of the tanks
    tanks = []

    # Read the input
    for i in range(n):
        tank_position = int(input())
        tanks.append(tank_position)

    # Initialize a set to store the positions of the bombs
    bombs = set()

    # Initialize a variable to store the minimum number of bombs
    min_bombs = 0

    # Iterate through the tanks and determine the minimum number of bombs needed to destroy all tanks
    for tank in tanks:
        # If the tank has not been destroyed, add its position to the set of bombs
        if tank not in bombs:
            bombs.add(tank)
            min_bombs += 1

            # If the tank is in the first or last cell, add the adjacent cell to the set of bombs
            if tank == 1 or tank == n:
                bombs.add(tank + 1)
                min_bombs += 1

    return min_bombs

def get_bomb_positions(n):
    # Initialize a list to store the positions of the tanks
    tanks = []

    # Read the input
    for i in range(n):
        tank_position = int(input())
        tanks.append(tank_position)

    # Initialize a set to store the positions of the bombs
    bombs = set()

    # Initialize a variable to store the minimum number of bombs
    min_bombs = 0

    # Iterate through the tanks and determine the minimum number of bombs needed to destroy all tanks
    for tank in tanks:
        # If the tank has not been destroyed, add its position to the set of bombs
        if tank not in bombs:
            bombs.add(tank)
            min_bombs += 1

            # If the tank is in the first or last cell, add the adjacent cell to the set of bombs
            if tank == 1 or tank == n:
                bombs.add(tank + 1)
                min_bombs += 1

    return list(bombs)

if __name__ == '__main__':
    n = int(input())
    min_bombs = get_minimum_bombs(n)
    bomb_positions = get_bomb_positions(n)
    print(min_bombs)
    for bomb_position in bomb_positions:
        print(bomb_position, end=" ")

