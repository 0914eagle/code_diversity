
def get_min_time(n, traffic_lights):
    # Initialize variables
    current_time = 0
    distance = 0
    max_speed = 1
    min_time = 0

    # Iterate through the traffic lights
    for i in range(n - 1):
        # Calculate the time it takes to pass the current light
        time_to_pass_light = max_speed * (traffic_lights[i][1] + traffic_lights[i][2])

        # Update the current time and distance
        current_time += time_to_pass_light
        distance += max_speed * traffic_lights[i][1]

        # Update the minimum time
        min_time = max(min_time, current_time + distance / max_speed)

        # Update the maximum speed
        max_speed = min(max_speed, traffic_lights[i][0])

    # Return the minimum time
    return min_time

def main():
    # Read the input
    n = int(input())
    traffic_lights = []
    for i in range(n - 1):
        traffic_lights.append([int(x) for x in input().split()])

    # Calculate the minimum time
    min_time = get_min_time(n, traffic_lights)

    # Print the result
    print(min_time)

if __name__ == '__main__':
    main()

