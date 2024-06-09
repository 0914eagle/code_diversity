
def get_rain_amount(d, t, c, r, clouds, roofs):
    # Initialize variables
    total_rain = 0
    current_time = 0
    current_position = 0
    roof_index = 0

    # Loop through each cloud
    for cloud in clouds:
        # Check if the cloud is in the zip code
        if cloud[2] > 0:
            # Check if the cloud is currently raining
            if current_time >= cloud[0] and current_time < cloud[1]:
                # Calculate the amount of rain that will fall on the current position
                rain_amount = cloud[3] * (min(current_position, d) - max(0, current_position - d))
                total_rain += rain_amount

        # Update the current time and position
        current_time += 1
        current_position += 1

        # Check if the current position is under a roof
        if current_position in roofs:
            # Skip over the roof segment
            current_position = roofs[current_position]

    return total_rain

def main():
    d, t, c, r = map(int, input().split())
    clouds = []
    for i in range(c):
        s, e, p, a = map(int, input().split())
        clouds.append([s, e, p, a])
    roofs = []
    for i in range(r):
        x, y = map(int, input().split())
        roofs.append([x, y])
    print(get_rain_amount(d, t, c, r, clouds, roofs))

if __name__ == '__main__':
    main()

