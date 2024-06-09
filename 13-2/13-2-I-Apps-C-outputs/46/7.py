
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
        # If the cloud is within the time frame
        if s <= t and e <= t:
            # Add the rain amount to the minimum rain
            min_rain += a * (e - s) * p
        # If the cloud starts before the time frame and ends after the time frame
        elif s < t and e > t:
            # Add the rain amount for the time frame to the minimum rain
            min_rain += a * (t - s) * p
        # If the cloud starts after the time frame
        else:
            continue

    # Loop through the roofs
    for i in range(r):
        x, y = roofs[i]
        # If the roof starts before the current position and ends after the current position
        if x <= current_position and y >= current_position:
            # Update the current position and roof index
            current_position = y
            roof_index = i
        # If the roof starts after the current position
        elif x > current_position:
            # Update the current position and roof index
            current_position = x
            roof_index = i

    # Return the minimum rain
    return min_rain

