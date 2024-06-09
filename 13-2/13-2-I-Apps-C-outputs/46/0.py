
def get_min_rain(d, t, c, r, clouds, roofs):
    # Initialize variables
    min_rain = 0
    current_time = 0
    current_position = 0
    roof_index = 0
    roof_start = 0
    roof_end = 0

    # Sort the clouds by starting time
    clouds.sort(key=lambda x: x[0])

    # Loop through the clouds
    for cloud in clouds:
        s, e, p, a = cloud
        # Check if the cloud is in the current zip code
        if current_position >= d:
            break
        # Check if the cloud is over the current position
        if current_position >= s and current_position < e:
            # Add the rain amount to the total rain
            min_rain += a
        # Check if the current time is greater than the cloud ending time
        if current_time >= e:
            continue
        # Check if the current position is within a roof segment
        while roof_index < r and current_position >= roof_end:
            roof_index += 1
            roof_start, roof_end = roofs[roof_index]
        if current_position >= roof_start and current_position < roof_end:
            # Add the rain amount to the total rain
            min_rain += a
        # Update the current time and position
        current_time = e
        current_position = current_position + (current_time - s) * 1

    return min_rain

