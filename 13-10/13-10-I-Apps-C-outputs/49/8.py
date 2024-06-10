
def get_min_time(n, traffic_lights):
    # Initialize variables
    min_time = 0
    current_time = 0
    current_speed = 0
    current_distance = 0

    # Loop through the traffic lights
    for traffic_light in traffic_lights:
        t, g, r = traffic_light
        green_time = t + g
        red_time = t + g + r

        # If the current time is before the green time, accelerate
        if current_time < green_time:
            current_speed += 1
            current_distance += current_speed

        # If the current time is during the green time, maintain speed
        elif current_time < green_time + r:
            current_distance += current_speed

        # If the current time is after the red time, decelerate
        else:
            current_speed -= 1
            current_distance += current_speed

        # Update the current time
        current_time = green_time + r

        # Check if the current distance is greater than the total distance
        if current_distance > n:
            return -1

    # Return the minimum time
    return current_time

def main():
    n = int(input())
    traffic_lights = []
    for i in range(n-1):
        t, g, r = map(int, input().split())
        traffic_lights.append((t, g, r))
    print(get_min_time(n, traffic_lights))

if __name__ == '__main__':
    main()

