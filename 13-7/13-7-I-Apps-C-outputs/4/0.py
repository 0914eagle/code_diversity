
def get_max_gems(n, r, w, h, gems):
    # Initialize variables
    max_gems = 0
    current_gems = 0
    current_position = (0, 0)
    current_velocity = (0, v)

    # Sort the gems by their y-coordinate in descending order
    gems.sort(key=lambda x: x[1], reverse=True)

    # Loop through the gems and try to collect them
    for gem in gems:
        # Calculate the distance to the gem
        distance = abs(current_position[1] - gem[1])

        # Calculate the time it will take to reach the gem
        time = distance / current_velocity[1]

        # Calculate the horizontal velocity required to reach the gem
        horizontal_velocity = (gem[0] - current_position[0]) / time

        # Check if the horizontal velocity is within the allowed range
        if -v/r <= horizontal_velocity <= v/r:
            # Update the current position and velocity
            current_position = (gem[0], gem[1])
            current_velocity = (horizontal_velocity, current_velocity[1])
            current_gems += 1

        # Check if the current position is above the finish line
        if current_position[1] >= h:
            break

    # Return the maximum number of gems collected
    return current_gems

def main():
    # Read the input
    n, r, w, h = map(int, input().split())
    gems = []
    for _ in range(n):
        x, y = map(int, input().split())
        gems.append((x, y))

    # Call the get_max_gems function and print the result
    print(get_max_gems(n, r, w, h, gems))

if __name__ == '__main__':
    main()

