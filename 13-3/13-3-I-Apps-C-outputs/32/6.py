
def get_rain_amount(d, t, c, r, clouds, roofs):
    # Initialize variables
    total_rain = 0
    current_time = 0
    current_position = 0
    roof_index = 0

    # Loop through the clouds
    for cloud in clouds:
        # Check if the cloud is in the zip code
        if cloud[2] > 0:
            # Check if the cloud is currently raining
            if current_time >= cloud[0] and current_time < cloud[1]:
                # Calculate the amount of rain that will fall on the current position
                rain_amount = (cloud[3] / 1000) * (cloud[1] - current_time)
                total_rain += rain_amount

        # Check if the current position is under a roof
        if current_position in roofs:
            # Calculate the time it will take to reach the next roof segment
            time_to_next_roof = roofs[current_position][1] - current_position

            # Check if the time to the next roof segment is less than the time until the next cloud
            if time_to_next_roof < cloud[1] - current_time:
                # Update the current time and position
                current_time += time_to_next_roof
                current_position += time_to_next_roof

                # Break out of the loop if the current position is under a roof
                break

        # Update the current time and position
        current_time += 1
        current_position += 1

        # Check if the current position is under a roof
        if current_position in roofs:
            # Break out of the loop if the current position is under a roof
            break

    # Return the total rain amount
    return total_rain

def f1(...):
    # Read the input from stdin
    d, t, c, r = map(int, input().split())
    clouds = []
    for i in range(c):
        s, e, p, a = map(int, input().split())
        clouds.append([s, e, p, a])
    roofs = []
    for i in range(r):
        x, y = map(int, input().split())
        roofs.append([x, y])

    # Call the get_rain_amount function
    total_rain = get_rain_amount(d, t, c, r, clouds, roofs)

    # Print the output to stdout
    print(total_rain)

if __name__ == '__main__':
    f1()

