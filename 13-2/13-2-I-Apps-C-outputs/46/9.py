
def get_min_rain(d, t, c, r, clouds, roofs):
    # Initialize variables
    min_rain = 0
    current_time = 0
    current_position = 0
    roof_index = 0
    roof_start = 0
    roof_end = 0

    # Sort the clouds by their start time
    clouds.sort(key=lambda x: x[0])

    # Loop through the clouds
    for cloud in clouds:
        s, e, p, a = cloud
        # If the cloud is within the time frame
        if s <= t and e <= t:
            # Add the rain amount to the minimum rain
            min_rain += a * (e - s) * p
        # If the cloud starts before the time frame and ends after the time frame
        elif s < t and e > t:
            # Add the rain amount for the time frame to the minimum rain
            min_rain += a * (t - s) * p
        # If the cloud starts after the time frame
        elif s > t:
            break

    # Loop through the roofs
    while roof_index < len(roofs) and current_position < d:
        # Get the start and end positions of the current roof
        roof_start, roof_end = roofs[roof_index]
        # If the current position is within the current roof
        if current_position >= roof_start and current_position < roof_end:
            # Add the rain amount for the time frame to the minimum rain
            min_rain += a * (t - current_time) * p
            # Break out of the loop
            break
        # If the current position is after the current roof
        elif current_position > roof_end:
            # Increment the current position and time
            current_position += 1
            current_time += 1
        # If the current position is before the current roof
        elif current_position < roof_start:
            # Increment the current position and time
            current_position += 1
            current_time += 1

    # Return the minimum rain
    return min_rain

