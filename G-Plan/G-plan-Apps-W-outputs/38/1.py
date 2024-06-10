ulate_water_level(leak_height, leak_rate, rainfall_duration, time_to_observation, observed_water_level, rainfall):
    water_level = 0
    for t in range(rainfall_duration + time_to_observation + 1):
        if t <= rainfall_duration:
            water_level += rainfall - leak_rate
        else:
            water_level -= leak_rate
        if water_level > leak_height:
            water_level = leak_height
    return water_level

def find_smallest_rainfall(leak_height, leak_rate, rainfall_duration, time_to_observation, observed_water_level):
    low = 0
    high = observed_water_level + leak_rate * (rainfall_duration + time_to_observation)
    while low < high:
        mid = (low + high) / 2
        water_level = calculate_water_level(leak_height, leak_rate, rainfall_duration, time_to_observation, observed_water_level, mid)
        if water_level < observed_water_level:
            low = mid + 0.000001
        else:
            high = mid
    return low

def find_largest_rainfall(leak_height, leak_rate, rainfall_duration, time_to_observation, observed_water_level):
    low = 0
    high = observed_water_level + leak_rate * (rainfall_duration + time_to_observation)
    while low < high:
        mid = (low + high) / 2
        water_level = calculate_water_level(leak_height, leak_rate, rainfall_duration, time_to_observation, observed_water_level, mid)
        if water_level <= observed_water_level:
            low = mid + 0.000001
        else:
            high = mid
    return low

if __name__ == "__main__":
    leak_height, leak_rate, rainfall_duration, time_to_observation, observed_water_level = map(float, input().split())
    smallest_rainfall = find_smallest_rainfall(leak_height, leak_rate, rainfall_duration, time_to_observation, observed_water_level)
    largest_rainfall = find_largest_rainfall(leak_height, leak_rate, rainfall_duration, time_to_observation, observed_water_level)
    print("{:.6f} {:.6f}".format(smallest_rainfall, largest_rainfall))
""