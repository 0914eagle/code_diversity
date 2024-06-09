
def get_rain_amount(d, t, c, r, clouds, roofs):
    # Initialize variables
    total_rain = 0
    current_time = 0
    current_position = 0
    roof_index = 0

    # Loop through each cloud
    for cloud in clouds:
        s, e, p, a = cloud
        # Check if the cloud is in the current zip code
        if current_position >= s and current_position <= e:
            # Check if the cloud is raining
            if current_time >= s and current_time <= e:
                # Add the rain amount to the total
                total_rain += a
        # Update the current time and position
        current_time += 1
        current_position += 1
        # Check if the current position is under a roof
        if current_position in roofs:
            # Add the rain amount to the total
            total_rain += a
            # Update the current position
            current_position += 1

    return total_rain

def main():
    d, t, c, r = map(int, input().split())
    clouds = []
    for i in range(c):
        s, e, p, a = map(int, input().split())
        clouds.append((s, e, p, a))
    roofs = []
    for i in range(r):
        x, y = map(int, input().split())
        roofs.append((x, y))
    print(get_rain_amount(d, t, c, r, clouds, roofs))

if __name__ == '__main__':
    main()

