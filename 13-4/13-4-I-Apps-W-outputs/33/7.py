
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
        # Find the closest tank to the current bomb position
        closest_tank = find_closest_tank(tanks, bombs)

        # Add the position of the closest tank to the list of bombs
        bombs.append(closest_tank)

        # Remove the closest tank from the list of tanks
        tanks.remove(closest_tank)

    # Return the minimum number of bombs needed to destroy all tanks
    return len(bombs)

def find_closest_tank(tanks, bombs):
    # Initialize the minimum distance to a large value
    min_distance = float('inf')

    # Initialize the position of the closest tank to -1
    closest_tank = -1

    # Loop through the tanks and find the closest one to the current bomb position
    for i in range(len(tanks)):
        # Calculate the distance between the current tank and the current bomb position
        distance = abs(tanks[i] - bombs[-1])

        # If the distance is less than the minimum distance, update the minimum distance and the position of the closest tank
        if distance < min_distance:
            min_distance = distance
            closest_tank = tanks[i]

    # Return the position of the closest tank
    return closest_tank

if __name__ == '__main__':
    n = int(input())
    print(get_minimum_bombs(n))

