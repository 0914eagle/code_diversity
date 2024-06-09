
def get_min_rain(d, t, c, r, clouds, roofs):
    # Initialize variables
    min_rain = 0
    current_time = 0
    current_position = 0
    roof_index = 0
    roof_start = 0
    roof_end = 0

    # Sort the clouds by start time
    clouds.sort(key=lambda x: x[0])

    # Loop through the clouds
    for cloud in clouds:
        start_time, end_time, probability, amount = cloud

        # Check if the cloud is in the current zip code
        if current_position >= d:
            break

        # Check if the cloud is in the current roof segment
        if roof_index < r and current_position >= roof_start and current_position < roof_end:
            min_rain += amount * (min(end_time, t) - current_time) * probability

        # Update the current time and position
        current_time = min(end_time, t)
        current_position += (current_time - start_time) * 1

        # Update the roof index and positions
        if roof_index < r and current_position >= roof_end:
            roof_index += 1
            roof_start, roof_end = roofs[roof_index]

    return min_rain

