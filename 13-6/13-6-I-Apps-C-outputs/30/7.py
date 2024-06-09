
def solve(n, s, lights):
    # Initialize the maximum number of on lights
    max_on = 0
    # Initialize a dictionary to store the on/off state of each light
    light_state = {}
    # Initialize a set to store the seconds when a light is on
    on_seconds = set()

    # Iterate over the lights
    for i in range(n):
        # Get the parameters of the current light
        a, b = lights[i]
        # Get the state of the current light (on/off)
        state = s[i]

        # If the light is on, add its second to the set of on seconds
        if state == "1":
            on_seconds.add(b)

        # Iterate over the seconds when the light is on
        for second in range(b, b + a * n, a):
            # If the light is on, add its second to the set of on seconds
            if state == "1":
                on_seconds.add(second)
            # If the light is off, remove its second from the set of on seconds
            else:
                on_seconds.discard(second)

        # Update the maximum number of on lights
        max_on = max(max_on, len(on_seconds))

    return max_on

