
def solve(d, t, c, r, clouds, roofs):
    # Initialize variables
    total_rain = 0
    current_time = 0
    current_position = 0
    roof_index = 0
    roof_start = 0
    roof_end = 0

    # Sort the clouds by their start time
    clouds.sort(key=lambda x: x[0])

    # Iterate through the clouds
    for cloud in clouds:
        s, e, p, a = cloud
        # If the cloud is within the time window
        if s <= current_time < e:
            # If the cloud is in your zip code
            if p > 0:
                # Calculate the amount of rain that will fall during the time window
                rain = (e - current_time) * a * p
                # Add the rain to the total
                total_rain += rain
        # If the current time is greater than the end time of the cloud
        if current_time >= e:
            # Move to the next cloud
            continue
        # If the current position is within a roof segment
        if current_position >= roof_start and current_position < roof_end:
            # Calculate the time it will take to reach the end of the roof segment
            time_to_end = roof_end - current_position
            # Add the time to the current time
            current_time += time_to_end
            # Move to the next roof segment
            roof_index += 1
            # If there are no more roof segments, break
            if roof_index >= len(roofs):
                break
            # Update the current position and end of the roof segment
            current_position = roofs[roof_index][0]
            roof_end = roofs[roof_index][1]
        # Calculate the time it will take to reach the end of the current segment
        time_to_end = d - current_position
        # Add the time to the current time
        current_time += time_to_end
        # Move to the next segment
        current_position = d

    # Return the total rain
    return total_rain

