
def get_min_rainfall(d, t, c, r, clouds, roofs):
    # Initialize variables
    min_rainfall = 0
    current_time = 0
    inside_roof = False

    # Sort the clouds by their starting time
    clouds = sorted(clouds, key=lambda x: x[0])

    # Iterate through the clouds
    for cloud in clouds:
        start_time, end_time, prob, rain = cloud

        # Check if the cloud is within the time frame
        if start_time <= current_time <= end_time:
            # Check if the cloud is in the zip code
            if prob > 0:
                # Add the rain to the min_rainfall
                min_rainfall += prob * rain

        # Check if the current time is within the roof segments
        for roof in roofs:
            x, y = roof
            if x <= current_time <= y:
                inside_roof = True
                break

        # Check if the current time is outside the roof segments
        if not inside_roof and current_time > y:
            inside_roof = False

        # Update the current time
        current_time = min(current_time + 1, t)

    # Return the min_rainfall
    return min_rainfall

