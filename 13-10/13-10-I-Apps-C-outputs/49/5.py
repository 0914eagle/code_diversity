
def get_time_required(n, traffic_lights):
    # Initialize variables
    time_required = 0
    current_time = 0
    previous_light = "green"

    # Iterate through each traffic light
    for i in range(n - 1):
        light = traffic_lights[i]
        t, g, r = light

        # If the previous light was green and the current light is red, accelerate
        if previous_light == "green" and light == "red":
            time_required += t
            current_time += t

        # If the previous light was red and the current light is green, decelerate
        elif previous_light == "red" and light == "green":
            time_required += t
            current_time += t

        # If the previous light was green and the current light is green, continue driving at a constant speed
        elif previous_light == "green" and light == "green":
            time_required += g
            current_time += g

        # If the previous light was red and the current light is red, stop driving
        elif previous_light == "red" and light == "red":
            time_required += r
            current_time += r

        # Update the previous light
        previous_light = light

    # Return the minimum time required to reach the end of the road
    return time_required

def get_traffic_lights(n, traffic_lights):
    # Initialize variables
    traffic_lights_list = []

    # Iterate through each traffic light
    for i in range(n - 1):
        light = input().split()
        t, g, r = int(light[0]), int(light[1]), int(light[2])
        traffic_lights_list.append((t, g, r))

    # Return the list of traffic lights
    return traffic_lights_list

if __name__ == '__main__':
    n = int(input())
    traffic_lights = get_traffic_lights(n, [])
    time_required = get_time_required(n, traffic_lights)
    print(time_required)

