
def calculate_max_minions(n_villages, m_minions, r_radius):
    # Initialize variables
    villages = []
    minions = []
    max_minions = 0

    # Iterate through the input data
    for i in range(n_villages):
        # Read the village location and radius
        vx, vy, vr = map(int, input().split())

        # Add the village to the list of villages
        villages.append((vx, vy, vr))

    for i in range(m_minions):
        # Read the minion location
        mx, my = map(int, input().split())

        # Add the minion to the list of minions
        minions.append((mx, my))

    # Iterate through the minions
    for minion in minions:
        # Initialize variables
        num_minions = 0
        radius = 0

        # Iterate through the villages
        for village in villages:
            # Calculate the distance between the minion and the village
            distance = math.sqrt((minion[0] - village[0]) ** 2 + (minion[1] - village[1]) ** 2)

            # Check if the minion is within the village's radius
            if distance <= village[2]:
                # Increment the number of minions
                num_minions += 1

                # Update the radius if necessary
                radius = max(radius, distance)

        # Check if the minion is within the maximum radius
        if radius <= r_radius:
            # Increment the maximum number of minions
            max_minions += 1

    return max_minions

def main():
    # Read the input data
    n_villages, m_minions, r_radius = map(int, input().split())

    # Calculate the maximum number of minions
    max_minions = calculate_max_minions(n_villages, m_minions, r_radius)

    # Print the result
    print(max_minions)

if __name__ == '__main__':
    main()

