
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
        # Find the tank with the minimum position
        min_tank = min(tanks)

        # Add the position of the minimum tank to the list of bombs
        bombs.append(min_tank)

        # Remove the minimum tank from the list of tanks
        tanks.remove(min_tank)

    # Return the list of bombs
    return bombs

def main():
    # Read the input from stdin
    n = int(input())

    # Call the get_minimum_bombs function and store the result in a variable
    bombs = get_minimum_bombs(n)

    # Print the number of bombs needed to destroy all tanks
    print(len(bombs))

    # Print the positions of the bombs
    for bomb in bombs:
        print(bomb, end=" ")

if __name__ == '__main__':
    main()

