
def get_rain_amount(d, t, c, r, clouds, roofs):
    # Initialize variables
    rain_amount = 0
    current_time = 0
    current_position = 0
    roof_index = 0

    # Loop through the clouds
    for cloud in clouds:
        # Check if the cloud is in the zip code
        if cloud[2] > 0:
            # Check if the cloud is currently raining
            if current_time >= cloud[0] and current_time < cloud[1]:
                # Add the rain amount to the total
                rain_amount += cloud[3]

        # Check if the current position is under a roof
        if current_position in roofs:
            # Add the rain amount to the total
            rain_amount += cloud[3]

        # Update the current time and position
        current_time += 1
        current_position += 1

        # Check if the current position is beyond the bus stop
        if current_position > d:
            break

    return rain_amount

def main():
    d, t, c, r = map(int, input().split())
    clouds = []
    for i in range(c):
        s, e, p, a = map(int, input().split())
        clouds.append([s, e, p, a])
    roofs = []
    for i in range(r):
        x, y = map(int, input().split())
        roofs.append(x)
        roofs.append(y)
    print(get_rain_amount(d, t, c, r, clouds, roofs))

if __name__ == '__main__':
    main()

