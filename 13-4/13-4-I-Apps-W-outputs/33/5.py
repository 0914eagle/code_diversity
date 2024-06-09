
def get_minimum_bombs(n):
    # Initialize a list to store the positions of the tanks
    tanks = []

    # Read the input from stdin
    for i in range(n):
        tank = int(input())
        tanks.append(tank)

    # Initialize a list to store the positions of the bombs
    bombs = []

    # Loop through the tanks and find the minimum number of bombs needed to destroy all tanks
    while len(tanks) > 0:
        # Find the tank with the minimum distance from the current bomb position
        min_distance = float('inf')
        min_tank = -1
        for i in range(len(tanks)):
            distance = abs(tanks[i] - bombs[-1])
            if distance < min_distance:
                min_distance = distance
                min_tank = i

        # Add the minimum tank to the list of destroyed tanks
        destroyed_tank = tanks.pop(min_tank)
        bombs.append(destroyed_tank)

    # Return the minimum number of bombs needed to destroy all tanks
    return len(bombs)

def main():
    n = int(input())
    print(get_minimum_bombs(n))

if __name__ == '__main__':
    main()

