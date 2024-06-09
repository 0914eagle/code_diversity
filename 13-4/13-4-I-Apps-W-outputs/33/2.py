
def get_min_bombs(n):
    # Initialize a list to store the positions of the tanks
    tanks = []

    # Read the input from stdin
    for i in range(n):
        tank = int(input())
        tanks.append(tank)

    # Initialize a variable to store the minimum number of bombs
    min_bombs = 0

    # Iterate through the tanks and count the number of bombs needed to destroy each tank
    for i in range(n):
        # If the tank has not been destroyed, add 1 to the minimum number of bombs
        if tanks[i] > 0:
            min_bombs += 1

            # If the tank has been destroyed, set its position to 0
            tanks[i] = 0

            # Iterate through the tanks again and move any tanks that are in the same cell as the destroyed tank
            for j in range(n):
                if tanks[j] > 0 and j == i:
                    tanks[j] = 0

    return min_bombs

def main():
    n = int(input())
    print(get_min_bombs(n))

if __name__ == '__main__':
    main()

