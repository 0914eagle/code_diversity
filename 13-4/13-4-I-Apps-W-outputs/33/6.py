
def get_map_size():
    return int(input())

def get_tank_positions(n):
    return [int(i) for i in input().split()]

def solve(n, tank_positions):
    # Initialize the number of bombs needed to destroy all tanks
    num_bombs = 0
    # Initialize the positions of the bombs
    bomb_positions = []
    # Loop through each tank position
    for tank_position in tank_positions:
        # If the tank position is not already in the bomb positions, add it
        if tank_position not in bomb_positions:
            num_bombs += 1
            bomb_positions.append(tank_position)
    # Return the number of bombs needed and the positions of the bombs
    return num_bombs, bomb_positions

if __name__ == '__main__':
    n = get_map_size()
    tank_positions = get_tank_positions(n)
    num_bombs, bomb_positions = solve(n, tank_positions)
    print(num_bombs)
    print(" ".join(str(bomb_position) for bomb_position in bomb_positions))

