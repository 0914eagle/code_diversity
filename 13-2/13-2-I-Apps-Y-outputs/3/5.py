
def get_speed(photographs):
    # Initialize variables
    previous_time = 0
    previous_distance = 0
    max_speed = 0

    # Iterate through the photographs
    for photograph in photographs:
        # Get the current time and distance
        current_time = photograph[0]
        current_distance = photograph[1]

        # Calculate the time difference and distance difference
        time_difference = current_time - previous_time
        distance_difference = current_distance - previous_distance

        # Calculate the speed
        speed = distance_difference / time_difference

        # Update the maximum speed
        max_speed = max(max_speed, speed)

        # Update the previous time and distance
        previous_time = current_time
        previous_distance = current_distance

    # Return the maximum speed
    return max_speed

def main():
    # Read the number of photographs
    n = int(input())

    # Read the photographs
    photographs = []
    for i in range(n):
        t, d = map(int, input().split())
        photographs.append((t, d))

    # Calculate the speed
    speed = get_speed(photographs)

    # Print the speed
    print(int(speed))

if __name__ == '__main__':
    main()

