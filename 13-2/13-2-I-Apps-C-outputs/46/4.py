
def get_min_rain(d, t, c, r, clouds, roofs):
    # Initialize variables
    min_rain = 0
    current_time = 0
    current_position = 0
    roof_index = 0
    roof_start = 0
    roof_end = 0

    # Sort the clouds by their starting time
    clouds.sort(key=lambda x: x[0])

    # Loop through the clouds
    for cloud in clouds:
        s, e, p, a = cloud
        # If the cloud is in the current zip code and the current time is within its raining period
        if p > 0 and current_time >= s and current_time < e:
            # Add the amount of rain from the cloud to the total rain
            min_rain += a * (min(e, current_time + 1) - current_time)
        # If the current time is greater than the end time of the cloud
        if current_time >= e:
            # Move on to the next cloud
            continue
        # If the current position is within a roof segment
        if current_position >= roof_start and current_position < roof_end:
            # Move on to the next roof segment
            roof_index += 1
            if roof_index < len(roofs):
                roof_start, roof_end = roofs[roof_index]
            else:
                roof_start, roof_end = 0, 0
        # If the current position is not within a roof segment and the current time is less than the end time of the cloud
        elif current_position < roof_start and current_time < e:
            # Move on to the next position
            current_position += 1
    
    return min_rain

