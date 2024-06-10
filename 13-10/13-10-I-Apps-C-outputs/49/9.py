
def get_min_time(n, traffic_lights):
    # Initialize variables
    current_time = 0
    total_time = 0
    distance_travelled = 0
    lights = []

    # Add the starting green light
    lights.append((0, "green"))

    # Loop through each traffic light
    for i in range(n - 1):
        # Add the current light to the list of lights
        lights.append((traffic_lights[i][0], "green" if traffic_lights[i][1] > traffic_lights[i][2] else "red"))

        # Update the current time
        current_time += traffic_lights[i][1]

        # If the current light is green, update the distance travelled
        if lights[-2][1] == "green":
            distance_travelled += 1

        # Add the next light to the list of lights
        lights.append((traffic_lights[i][0] + traffic_lights[i][1] + traffic_lights[i][2], "red"))

        # Update the current time
        current_time += traffic_lights[i][2]

    # Add the ending green light
    lights.append((traffic_lights[-1][0] + traffic_lights[-1][1] + traffic_lights[-1][2], "green"))

    # Loop through each light and calculate the time until the next green light
    for i in range(len(lights) - 1):
        # If the current light is green, calculate the time until the next green light
        if lights[i][1] == "green":
            total_time += min(lights[i + 1][0] - lights[i][0], lights[i + 1][0] - lights[i][0] - distance_travelled)

    # Return the minimum time required to reach the end of the road
    return total_time

def main():
    n = int(input())
    traffic_lights = []
    for i in range(n - 1):
        traffic_lights.append(list(map(int, input().split())))
    print(get_min_time(n, traffic_lights))

if __name__ == '__main__':
    main()

