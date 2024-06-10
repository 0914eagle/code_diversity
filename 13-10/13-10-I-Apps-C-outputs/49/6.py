
def calculate_time(n, lights):
    # Initialize variables
    time = 0
    distance = 0
    current_light = 0
    acceleration = 1
    velocity = 0

    # Loop through each light
    for i in range(n):
        # Update time and distance
        time += lights[i][1] + lights[i][2]
        distance += lights[i][1] * acceleration

        # Update velocity
        velocity = acceleration * time

        # Check if we need to pass the light
        if current_light != i:
            # Add the time to pass the light
            time += lights[i][0]

            # Update current light
            current_light = i

    # Add the time to pass the final light
    time += lights[n - 1][0]

    return time

def main():
    n = int(input())
    lights = []
    for i in range(n - 1):
        t, g, r = map(int, input().split())
        lights.append((t, g, r))
    print(calculate_time(n, lights))

if __name__ == '__main__':
    main()

