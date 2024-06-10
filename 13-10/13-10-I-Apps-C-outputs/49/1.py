
def get_input():
    n = int(input())
    lights = []
    for i in range(n-1):
        t, g, r = map(int, input().split())
        lights.append([t, g, r])
    return n, lights

def solve(n, lights):
    # Initialize variables
    min_time = 0
    current_time = 0
    current_speed = 0
    total_distance = n
    
    # Iterate through the lights
    for light in lights:
        t, g, r = light
        # Calculate the time it takes to pass the light
        time_to_pass_light = g + r
        # Calculate the speed at which the car should accelerate to pass the light
        required_speed = t / time_to_pass_light
        # Calculate the time it takes to accelerate to the required speed
        time_to_accelerate = (required_speed - current_speed) / 1
        # Calculate the total time it takes to pass the light
        total_time = time_to_accelerate + time_to_pass_light
        # Update the current time and speed
        current_time += total_time
        current_speed = required_speed
        # Update the minimum time
        min_time = max(min_time, current_time)
    
    # Return the minimum time required to reach the end of the road
    return min_time + total_distance

def main():
    n, lights = get_input()
    print(solve(n, lights))

if __name__ == '__main__':
    main()

