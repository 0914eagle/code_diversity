
def get_min_rain(d, t, c, r, clouds, roofs):
    # Initialize variables
    min_rain = 0
    curr_time = 0
    rain_intensity = 0
    rain_probability = 0
    rain_duration = 0
    roof_start = 0
    roof_end = 0

    # Loop through the clouds
    for i in range(c):
        # Get the cloud information
        s, e, p, a = clouds[i]

        # Check if the cloud is within the time frame
        if s <= t and e <= t:
            # Calculate the rain intensity and probability
            rain_intensity += a
            rain_probability += p
            rain_duration += e - s

    # Loop through the roofs
    for i in range(r):
        # Get the roof information
        x, y = roofs[i]

        # Check if the roof overlaps with the time frame
        if x <= t and y >= t:
            # Calculate the roof start and end times
            roof_start = max(x, curr_time)
            roof_end = min(y, t)

            # Calculate the rain intensity and probability during the roof period
            rain_intensity += (roof_end - roof_start) * rain_intensity / rain_duration
            rain_probability += (roof_end - roof_start) * rain_probability / rain_duration

            # Update the current time
            curr_time = roof_end

    # Calculate the minimum rain intensity
    min_rain = rain_intensity * rain_probability

    # Return the minimum rain intensity
    return min_rain

