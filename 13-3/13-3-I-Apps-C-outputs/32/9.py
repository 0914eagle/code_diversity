
def get_min_rain_amount(d, t, c, r, clouds, roofs):
    # Initialize variables
    min_rain_amount = 0
    current_time = 0
    current_position = 0
    current_roof = 0

    # Sort the clouds by their starting time
    clouds.sort(key=lambda x: x[0])

    # Loop through the clouds
    for cloud in clouds:
        # Check if the cloud is in the current zip code
        if cloud[2] > 0:
            # Check if the cloud is currently raining
            if current_time >= cloud[0] and current_time < cloud[1]:
                # Add the rain amount to the total rain amount
                min_rain_amount += cloud[3]

        # Check if the current position is under a roof
        if current_position in roofs[current_roof]:
            # Add the rain amount to the total rain amount
            min_rain_amount += cloud[3]

        # Update the current time and position
        current_time = cloud[1]
        current_position = d - current_time * 1

        # Check if the current roof has ended
        if current_position in roofs[current_roof]:
            current_roof += 1

    return min_rain_amount

def main():
    d, t, c, r = map(int, input().split())
    clouds = []
    for i in range(c):
        s, e, p, a = map(float, input().split())
        clouds.append([s, e, p, a])
    roofs = []
    for i in range(r):
        x, y = map(int, input().split())
        roofs.append([x, y])
    print(get_min_rain_amount(d, t, c, r, clouds, roofs))

if __name__ == '__main__':
    main()

