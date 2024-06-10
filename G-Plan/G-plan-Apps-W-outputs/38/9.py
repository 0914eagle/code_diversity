
def calculate_rainfall_leak_range(leak_height, leak_rate, rainfall_duration, time_to_observation, observed_water_level):
    def calculate_water_level(rainfall_amount):
        water_level = 0
        for t in range(int(rainfall_duration) + 1):
            water_level += rainfall_amount
            if water_level > leak_height:
                water_level -= leak_rate
            if t == int(rainfall_duration):
                water_level -= leak_rate * (time_to_observation - rainfall_duration)
        return water_level

    lower_bound = max(0, observed_water_level - leak_rate * time_to_observation)
    upper_bound = observed_water_level + leak_rate * (rainfall_duration + time_to_observation)

    while calculate_water_level(lower_bound) < observed_water_level:
        lower_bound += 0.000001

    while calculate_water_level(upper_bound) > observed_water_level:
        upper_bound -= 0.000001

    return lower_bound, upper_bound

if __name__ == "__main__":
    leak_height, leak_rate, rainfall_duration, time_to_observation, observed_water_level = map(float, input().split())
    result = calculate_rainfall_leak_range(leak_height, leak_rate, rainfall_duration, time_to_observation, observed_water_level)
    print("{:.6f} {:.6f}".format(result[0], result[1]))
