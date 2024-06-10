ulate_water_level(leak_height, leak_rate, rainfall_duration, time_to_observation, observed_water_level, rainfall):
    water_level = 0
    if rainfall > 0:
        for t in range(int(rainfall_duration) + int(time_to_observation) + 1):
            if t <= int(rainfall_duration):
                water_level += rainfall - leak_rate
            elif t > int(rainfall_duration) and t <= int(rainfall_duration) + int(time_to_observation):
                water_level -= leak_rate
            if water_level < 0:
                water_level = 0
            if water_level > leak_height:
                water_level = leak_height
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
    largest_rainfall = find_largest_rainfall(leak_height, leak_rate, rainfall_duration, time_to_obsation, observed_water_level)
    print("{:.6f} {:.6f}".format(smallest_rainfall, largest_rainfall)) 
""