ulate_water_level(leak_height, leak_rate, rainfall_duration, time_to_observation, observed_water_level, rainfall):
    water_level = 0
    if rainfall <= time_to_observation * leak_rate:
        water_level = max(0, observed_water_level - (time_to_observation - rainfall) * leak_rate)
    else:
        water_level = observed_water_level + (rainfall - time_to_observation) - leak_height
    return water_level

def find_smallest_rainfall(leak_height, leak_rate, rainfall_duration, time_to_observation, observed_water_level):
    low = 0
    high = observed_water_level + leak_height + time_to_observation
    while low < high:
        mid = (low + high) / 2
        if calculate_water_level(leak_height, leak_rate, rainfall_duration, time_to_observation, observed_water_level, mid) >= 0:
            high = mid
        else:
            low = mid + 0.000001
    return low

def find_largest_rainfall(leak_height, leak_rate, rainfall_duration, time_to_observation, observed_water_level):
    low = 0
    high = observed_water_level + leak_height + time_to_observation
    while low < high:
        mid = (low + high) / 2
        if calculate_water_level(leak_height, leak_rate, rainfall_duration, time_to_observation, observed_water_level, mid) <= observed_water_level:
            low = mid
        else:
            high = mid - 0.000001
    return low

if __name__ == "__main__":
    leak_height, leak_rate, rainfall_duration, time_to_observation, observed_water_level = map(float, input().split())
    smallest_rainfall = find_smallest_rainfall(leak_height, leak_rate, rainfall_duration, time_to_observation, observed_water_level)
    largest_rainfall = find_largest_rainfall(leak_height, leak_rate, rainfall_duration, time_to_obsation, observed_water_level)
    print("{:.6f} {:.6f}".format(smallest_rainfall, largest_rainfall)) 
""