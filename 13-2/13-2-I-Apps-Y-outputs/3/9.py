
def get_speed(photos):
    # Initialize variables
    max_speed = 0
    current_speed = 0
    previous_distance = 0

    # Iterate through the photos
    for photo in photos:
        # Calculate the time and distance between this photo and the previous one
        time_diff = photo[0] - previous_distance
        distance_diff = photo[1] - previous_distance

        # Calculate the speed between this photo and the previous one
        speed = distance_diff / time_diff

        # Update the maximum speed if necessary
        if speed > max_speed:
            max_speed = speed

        # Update the previous distance and time
        previous_distance = photo[1]

    # Return the maximum speed
    return max_speed

def main():
    # Read the number of photos
    n = int(input())

    # Read the photos
    photos = []
    for i in range(n):
        t, d = map(int, input().split())
        photos.append((t, d))

    # Calculate the maximum speed
    max_speed = get_speed(photos)

    # Print the result
    print(max_speed)

if __name__ == '__main__':
    main()

