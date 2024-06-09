
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
        s, e, p, a = cloud
        # Check if the cloud is in the current zip code
        if p > 0:
            # Check if the cloud is currently raining
            if current_time >= s and current_time < e:
                # Add the rain amount to the total rain
                min_rain += a
            # Check if the cloud is about to start raining
            elif current_time == s:
                # Add the rain amount to the total rain
                min_rain += a
            # Check if the cloud has passed
            elif current_time > e:
                # Subtract the rain amount from the total rain
                min_rain -= a

        # Check if the current position is under a roof
        if current_position in roofs:
            # Check if the current position is the start of a roof
            if current_position == roof_start:
                # Set the current position to the end of the roof
                current_position = roof_end
            # Check if the current position is the end of a roof
            elif current_position == roof_end:
                # Set the current position to the start of the roof
                current_position = roof_start
            # Check if the current position is in the middle of a roof
            else:
                # Set the current position to the end of the roof
                current_position = roof_end

        # Check if the current time is greater than the time until the bus leaves
        if current_time >= t:
            # Break out of the loop
            break

        # Increment the current time and position
        current_time += 1
        current_position += 1

        # Check if the current position is at the bus stop
        if current_position == d:
            # Break out of the loop
            break

    # Return the minimum rain
    return min_rain

