ulate_water_level(leak_height, leak_rate, rainfall_duration, time_to_observation, observed_water_level, rainfall):
    water_level = 0
    if rainfall > 0:
        water_level = min(rainfall, leak_height) + (rainfall - min(rainfall, leak_height)) - leak_rate * max(0, rainfall_duration - time_to_observation)
    return water_level

def find_smallest_rainfall(leak_height, leak_rate, rainfall_duration, time_to_observation, observed_water_level):
    low = 0
    high = observed_water_level
    while low < high:
        mid = (low + high) / 2
        if calculate_water_level(leak_height, leak_rate, rainfall_duration, time_to_observation, observed_water_level, mid) < observed_water_level:
            low = mid + 0.000001
        else:
            high = mid
    return low

def find_largest_rainfall(leak_height, leak_rate, rainfall_duration, time_to_observation, observed_water_level):
    low = 0
    high = observed_water_level
    while low < high:
        mid = (low + high) / 2
        if calculate_water_level(leak_height, leak_rate, rainfall_duration, time_to_observation, observed_water_level, mid) <= observed_water_level:
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