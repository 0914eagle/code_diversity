
def solve(n, traffic_lights):
    # Initialize variables
    min_time = 0
    cur_time = 0
    cur_speed = 0
    cur_light = 0
    light_times = []

    # Add the starting time to the list of light times
    light_times.append(cur_time)

    # Loop through each traffic light
    for i in range(n - 1):
        # Update the current time and speed
        cur_time += cur_speed
        cur_speed = 1

        # Check if the current light is green
        if cur_light == i:
            # If so, update the current speed and light index
            cur_light += 1
            cur_speed = 0

        # Add the current time to the list of light times
        light_times.append(cur_time)

    # Calculate the minimum time to reach the end of the road
    for i in range(n - 1):
        # Calculate the time it takes to pass each light
        time_to_pass_light = light_times[i + 1] - light_times[i]

        # Check if the time to pass the light is less than the minimum time
        if time_to_pass_light < min_time:
            # If so, update the minimum time
            min_time = time_to_pass_light

    # Return the minimum time
    return min_time

def main():
    # Read the input
    n = int(input())
    traffic_lights = []
    for i in range(n - 1):
        traffic_lights.append(list(map(int, input().split())))

    # Call the solve function
    min_time = solve(n, traffic_lights)

    # Print the output
    print(min_time)

if __name__ == '__main__':
    main()

