
def get_tide_level(time, amplitude):
    return 0.5 * amplitude * (math.cos(time * 2 * math.pi / 12) + 1)

def get_safe_distance(home_coordinates, tide_levels, walking_speed):
    # Initialize variables
    distance = 0
    current_coordinates = home_coordinates
    previous_coordinates = home_coordinates
    tide_level = get_tide_level(0, amplitude)

    # Loop through the tide levels
    for i in range(1, len(tide_levels)):
        # Get the current tide level
        tide_level = get_tide_level(i, amplitude)

        # Get the coordinates of the current square
        current_coordinates = (current_coordinates[0] + 10, current_coordinates[1])

        # Check if the current square is dry
        if tide_levels[i] <= tide_level + 1:
            # If the current square is dry, update the distance
            distance += math.sqrt((current_coordinates[0] - previous_coordinates[0]) ** 2 + (current_coordinates[1] - previous_coordinates[1]) ** 2)
            previous_coordinates = current_coordinates

    # Return the safe distance
    return distance

def main():
    # Read input
    amplitude, walking_speed = map(float, input().split())
    width, height, x, y = map(int, input().split())
    tide_levels = []
    for i in range(height):
        tide_levels.extend(list(map(int, input().split())))

    # Get the safe distance
    safe_distance = get_safe_distance((x, y), tide_levels, walking_speed)

    # Print output
    print(safe_distance)

if __name__ == '__main__':
    main()

