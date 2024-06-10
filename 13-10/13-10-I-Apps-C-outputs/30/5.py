
import math

def get_max_minions(villages, minions, radius):
    # Initialize variables
    max_minions = 0
    destroyed_minions = set()

    # Loop through each village
    for village in villages:
        # Get the center of the village
        cx, cy = village[0], village[1]

        # Loop through each minion
        for minion in minions:
            # Get the distance between the minion and the village center
            dx, dy = minion[0] - cx, minion[1] - cy
            distance = math.sqrt(dx**2 + dy**2)

            # Check if the minion is inside the village
            if distance <= village[2] and distance <= radius:
                # Add the minion to the set of destroyed minions
                destroyed_minions.add(minion)

    # Return the number of destroyed minions
    return len(destroyed_minions)

def main():
    # Read the input
    n, m, r = map(int, input().split())
    villages = []
    for _ in range(n):
        villages.append(list(map(int, input().split())))
    minions = []
    for _ in range(m):
        minions.append(list(map(int, input().split())))

    # Call the function to get the maximum number of minions that can be destroyed
    max_minions = get_max_minions(villages, minions, r)

    # Print the output
    print(max_minions)

if __name__ == '__main__':
    main()

