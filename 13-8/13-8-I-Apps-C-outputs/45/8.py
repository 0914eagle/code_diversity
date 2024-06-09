
def solve(T, c, d):
    # Calculate the distance in kilometers
    distance = d / 1000

    # Calculate the minimum speed to cover the distance in the given time
    min_speed = distance / T

    # Initialize the rain and sweat accumulators
    rain = 0
    sweat = 0

    # Loop through each minute interval
    for i in range(T):
        # Calculate the rain accumulated during this minute
        rain += r_i

        # Calculate the sweat accumulated during this minute
        sweat += c * min_speed ** 2

    # Return the total rain and sweat accumulated
    return rain + sweat

