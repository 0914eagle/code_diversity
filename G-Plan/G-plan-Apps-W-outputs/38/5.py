
def calculate_rainfall(leak_height, leak_rate, rainfall_duration, time_to_observation, observed_water_level):
    smallest_rainfall = max(0, observed_water_level - leak_height - leak_rate * (rainfall_duration + time_to_observation))
    largest_rainfall = max(0, observed_water_level - leak_height)    
    return smallest_rainfall, largest_rainfall

if __name__ == "__main__":
    L, K, T1, T2, H = map(float, input().split())
    result = calculate_rainfall(L, K, T1, T2, H)
    print("{:.6f} {:.6f}".format(result[0], result[1]))
