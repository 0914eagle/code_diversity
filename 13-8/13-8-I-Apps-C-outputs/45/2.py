
def get_dry(T, c, d):
    # Initialize variables
    rain = [0] * T
    sweat = [0] * T
    speed = 0
    time = 0
    wetness = 0

    # Read rain data
    for i in range(T):
        rain[i] = float(input())

    # Calculate sweat intensity
    sweat_intensity = c * speed ** 2

    # Iterate through time
    while time < T:
        # Update sweat intensity
        sweat[time] = sweat_intensity

        # Update wetness
        wetness += rain[time] + sweat[time]

        # Update speed
        speed += 1

        # Update time
        time += 1

    # Calculate final wetness
    wetness += rain[time - 1] + sweat[time - 1]

    return wetness

