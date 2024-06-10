
def get_max_gems(n, r, w, h, gems):
    # Initialize variables
    max_gems = 0
    current_gems = 0
    current_position = (0, 0)
    vertical_velocity = 1
    horizontal_velocity = 0

    # Sort the gems by their y-coordinate in descending order
    gems = sorted(gems, key=lambda x: x[1], reverse=True)

    # Loop through the gems and try to collect them
    for gem in gems:
        # Calculate the distance to the current gem
        distance = abs(current_position[1] - gem[1])

        # Check if the gem is within reach
        if distance <= vertical_velocity:
            # Update the current position and number of gems collected
            current_position = gem
            current_gems += 1

            # Update the maximum number of gems if necessary
            if current_gems > max_gems:
                max_gems = current_gems

        # Check if the gem is out of reach
        else:
            # Update the vertical velocity if necessary
            if vertical_velocity < distance / r:
                vertical_velocity = distance / r

            # Update the current position and number of gems collected
            current_position = (current_position[0], current_position[1] - vertical_velocity)
            current_gems = 0

    return max_gems

def main():
    n, r, w, h = map(int, input().split())
    gems = []
    for _ in range(n):
        x, y = map(int, input().split())
        gems.append((x, y))
    max_gems = get_max_gems(n, r, w, h, gems)
    print(max_gems)

if __name__ == '__main__':
    main()

