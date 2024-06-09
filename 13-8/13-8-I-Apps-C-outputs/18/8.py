
def get_min_rain(d, t, c, r, clouds, roofs):
    # Initialize variables
    min_rain = 0
    current_time = 0
    current_rain = 0
    roof_index = 0

    # Sort the clouds by start time
    clouds.sort(key=lambda x: x[0])

    # Loop through the clouds
    for cloud in clouds:
        start_time, end_time, prob, amount = cloud
        current_time = max(current_time, start_time)
        if current_time <= t:
            if prob > 0:
                # Add the rain amount for the current time
                current_rain += prob * amount
            # Check if the current time is within a roof segment
            while roof_index < r and roofs[roof_index][0] <= current_time <= roofs[roof_index][1]:
                current_rain = max(current_rain, roofs[roof_index][2])
                roof_index += 1
            min_rain = max(min_rain, current_rain)
        current_time = end_time

    return min_rain

