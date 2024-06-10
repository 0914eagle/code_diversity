
def get_max_minions(n, m, r, villages, minions):
    # Initialize a list to store the destroyed minions
    destroyed_minions = []

    # Iterate over the villages
    for village in villages:
        # Get the village center and radius
        center_x, center_y, radius = village

        # Iterate over the minions
        for minion in minions:
            # Get the minion location
            minion_x, minion_y = minion

            # Check if the minion is within the attack range of the village
            if (minion_x - center_x) ** 2 + (minion_y - center_y) ** 2 <= radius ** 2:
                # Add the minion to the destroyed minions list
                destroyed_minions.append(minion)

    # Return the number of destroyed minions
    return len(destroyed_minions)

def main():
    # Read the input
    n, m, r = map(int, input().split())
    villages = []
    for i in range(n):
        village = tuple(map(int, input().split()))
        villages.append(village)
    minions = []
    for i in range(m):
        minion = tuple(map(int, input().split()))
        minions.append(minion)

    # Call the function to get the maximum number of minions that can be destroyed
    max_minions = get_max_minions(n, m, r, villages, minions)

    # Print the output
    print(max_minions)

if __name__ == '__main__':
    main()

