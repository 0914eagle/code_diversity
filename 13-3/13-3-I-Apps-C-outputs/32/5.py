
def get_expected_rainfall(d, t, c, r, clouds, roofs):
    # Initialize variables
    expected_rainfall = 0
    current_time = 0
    current_position = 0
    roof_index = 0

    # Loop through the clouds
    for cloud in clouds:
        # Check if the cloud is in the zip code
        if cloud[2] > 0:
            # Check if the cloud is currently raining
            if current_time >= cloud[0] and current_time < cloud[1]:
                # Calculate the amount of rain that will fall during the cloud's raining period
                rain_amount = cloud[3] * (cloud[1] - current_time)
                # Check if the rain will fall on the route to the bus stop
                if current_position + rain_amount > d:
                    # Calculate the amount of rain that will fall on the route to the bus stop
                    rain_amount = d - current_position
                # Add the rain amount to the expected rainfall
                expected_rainfall += rain_amount

        # Update the current time and position
        current_time = cloud[1]
        current_position += cloud[3] * (cloud[1] - cloud[0])

    # Loop through the roofs
    for roof in roofs:
        # Check if the roof is on the route to the bus stop
        if current_position >= roof[0] and current_position < roof[1]:
            # Calculate the amount of rain that will fall on the roof
            rain_amount = expected_rainfall - (current_position - roof[0]) * (current_position - roof[0])
            # Update the expected rainfall
            expected_rainfall = rain_amount
            # Break out of the loop
            break

    # Return the expected rainfall
    return expected_rainfall

def main():
    # Read input from stdin
    d, t, c, r = map(int, input().split())
    clouds = []
    for _ in range(c):
        clouds.append(list(map(int, input().split())))
    roofs = []
    for _ in range(r):
        roofs.append(list(map(int, input().split())))

    # Calculate the expected rainfall
    expected_rainfall = get_expected_rainfall(d, t, c, r, clouds, roofs)

    # Print the expected rainfall
    print(expected_rainfall)

if __name__ == '__main__':
    main()

