
def get_min_rain_expectation(d, t, c, r, clouds, roofs):
    # Initialize variables
    min_rain_expectation = 0
    current_time = 0
    current_rain_intensity = 0
    current_rain_probability = 0

    # Loop through the clouds
    for cloud in clouds:
        # Get the cloud parameters
        start_time, end_time, rain_probability, rain_intensity = cloud

        # Check if the cloud is currently raining
        if current_time >= start_time and current_time < end_time:
            # Add the current rain intensity to the total rain expectation
            min_rain_expectation += rain_intensity

        # Check if the cloud will be raining during the travel time
        if start_time < current_time + t and end_time > current_time + t:
            # Add the rain intensity to the total rain expectation
            min_rain_expectation += rain_intensity

    # Loop through the roofs
    for roof in roofs:
        # Get the roof parameters
        start_point, end_point = roof

        # Check if the bus stop is under the roof
        if start_point <= d and end_point > d:
            # Add the rain intensity to the total rain expectation
            min_rain_expectation += current_rain_intensity * current_rain_probability

    # Return the minimum rain expectation
    return min_rain_expectation

