
def get_dry(T, c, d, rain):
    # Calculate the distance you can cycle in each minute
    distance_per_minute = d / T

    # Calculate the speed you need to cycle at each minute to cover the distance
    speed_per_minute = distance_per_minute / (1 - c)

    # Calculate the time you need to cycle at each speed to cover the distance
    time_per_minute = distance_per_minute / speed_per_minute

    # Calculate the total time it takes to cycle home
    total_time = sum(time_per_minute)

    # Calculate the total rain and sweat you get wet from
    total_rain_and_sweat = sum(rain) + c * total_time ** 2

    return total_rain_and_sweat

