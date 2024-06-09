
def get_expected_rainfall(d, t, c, r, clouds, roofs):
    # Initialize variables
    expected_rainfall = 0
    current_time = 0
    current_position = 0
    current_roof = 0

    # Loop through the clouds
    for i in range(c):
        # Get the cloud information
        start_time, end_time, probability, amount = clouds[i]

        # Check if the cloud is in the current zip code
        if current_position >= start_time and current_position <= end_time:
            # Add the rain amount to the expected rainfall
            expected_rainfall += amount * probability

        # Update the current time and position
        current_time += 1
        current_position += 1

        # Check if the current position is under a roof
        if current_position == roofs[current_roof][0]:
            # Add the rain amount to the expected rainfall
            expected_rainfall += amount * (1 - probability)
            current_roof += 1

    # Return the expected rainfall
    return expected_rainfall

def main():
    # Read the input
    d, t, c, r = map(int, input().split())
    clouds = []
    for i in range(c):
        s, e, p, a = map(float, input().split())
        clouds.append((s, e, p, a))
    roofs = []
    for i in range(r):
        x, y = map(int, input().split())
        roofs.append((x, y))

    # Call the function to get the expected rainfall
    expected_rainfall = get_expected_rainfall(d, t, c, r, clouds, roofs)

    # Print the expected rainfall
    print(expected_rainfall)

if __name__ == '__main__':
    main()

