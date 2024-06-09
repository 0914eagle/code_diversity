
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
            # Calculate the amount of rain that will fall during the cloud's raining period
            rain_amount = (e - current_time) * a * p
            total_rain += rain_amount
        current_time = e
        current_position = e

    # Loop through each roof segment
    for roof in roofs:
        x, y = roof
        # Check if the current position is within the roof segment
        if current_position >= x and current_position <= y:
            # Calculate the amount of rain that will fall during the time the roof is open
            rain_amount = (y - current_position) * a * p
            total_rain += rain_amount
        current_position = y

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

