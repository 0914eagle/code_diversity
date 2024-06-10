ulate_water_level(leak_height, leak_rate, rainfall_duration, time_to_observation, rainfall_amount):
    water_level = 0
    if rainfall_duration > 0:
        water_level = min(rainfall_amount, leak_height) + (rainfall_duration - time_to_observation) * leak_rate
    return water_level

def find_smallest_largest_rainfall(leak_height, leak_rate, rainfall_duration, time_to_observation, observed_water_level):
    smallest_rainfall = max(0, observed_water_level - (rainfall_duration - time_to_observation) * leak_rate)
    largest_rainfall = min(observed_water_level, leak_height)
    return smallest_rainfall, largest_rainfall

if __name__ == "__main__":
    input_values = input().split()
    leak_height, leak_rate, rainfall_duration, time_to_observation, observed_water_level = map(float, input_values)

    smallest_rainfall, largest_rainfall = find_smallest_largest_rainfall(leak_height, leak_rate, rainfall_duration, time_to_observation, observed_water_level)

    print("{:.6f} {:.6f}".format(smallest_rainfall, largest_rainfall))
