
def get_min_time(n, traffic_lights):
    # Initialize variables
    current_time = 0
    total_time = 0
    is_accelerating = False

    # Loop through each traffic light
    for i in range(n - 1):
        t, g, r = traffic_lights[i]
        green_duration = t - current_time

        # If the light is green, accelerate
        if green_duration > 0:
            total_time += green_duration * 1.0
            current_time += green_duration
            is_accelerating = True

        # If the light is red, stop accelerating
        if green_duration < 0:
            is_accelerating = False

        # If the light is green and we are accelerating, add the acceleration time
        if is_accelerating:
            total_time += g / 1.0
            current_time += g

    # Add the time to reach the end of the road
    total_time += n - current_time

    return total_time

def main():
    n = int(input())
    traffic_lights = []
    for i in range(n - 1):
        t, g, r = map(int, input().split())
        traffic_lights.append((t, g, r))
    print(get_min_time(n, traffic_lights))

if __name__ == '__main__':
    main()

