
def get_dry_time(T, c, d):
    # Initialize variables
    rain_total = 0
    sweat_total = 0
    rain_array = []

    # Read input from stdin
    for i in range(T):
        rain_array.append(float(input()))

    # Calculate sweat rate
    sweat_rate = c * d ** 2

    # Calculate rain and sweat for each minute
    for i in range(T):
        rain_total += rain_array[i]
        sweat_total += sweat_rate * i

    # Return total rain and sweat
    return rain_total + sweat_total

