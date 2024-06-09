
def get_min_bombs(n):
    # Initialize a list to store the positions of the tanks
    tanks = []

    # Read the input
    for i in range(n):
        tank = int(input())
        tanks.append(tank)

    # Initialize a list to store the positions of the bombs
    bombs = []

    # Loop through the tanks and find the minimum number of bombs needed to destroy all tanks
    while len(tanks) > 0:
        # Find the tank with the minimum distance from the starting position
        min_dist = float('inf')
        for i in range(len(tanks)):
            dist = abs(tanks[i] - 1)
            if dist < min_dist:
                min_dist = dist
                min_tank = i

        # Add the position of the minimum tank to the list of bombs
        bombs.append(tanks[min_tank])
        tanks.pop(min_tank)

    return len(bombs)

def main():
    n = int(input())
    print(get_min_bombs(n))

if __name__ == '__main__':
    main()

