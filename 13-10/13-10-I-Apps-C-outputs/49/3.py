
def solve(n, lights):
    # Initialize variables
    min_time = 0
    cur_time = 0
    prev_light = 0
    speed = 1

    # Iterate through the lights
    for light in lights:
        # Calculate the time to pass the current light
        time_to_pass_light = (light[0] - prev_light) / speed

        # If the light is green, increase the current time by the time to pass the light
        if light[1] > 0:
            cur_time += time_to_pass_light

        # If the light is red, decrease the current time by the time to pass the light
        else:
            cur_time -= time_to_pass_light

        # Update the previous light time
        prev_light = light[0]

    # Return the minimum time required to reach the end of the road
    return cur_time

def main():
    n = int(input())
    lights = []
    for i in range(n-1):
        lights.append(list(map(int, input().split())))
    print(solve(n, lights))

if __name__ == '__main__':
    main()

