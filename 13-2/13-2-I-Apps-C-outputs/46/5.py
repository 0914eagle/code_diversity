
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
        current_time = s

        # Check if the cloud is in the current zip code
        if p > 0:
            # Calculate the amount of rain that will fall during the cloud's raining period
            rain_amount = a * (e - s)

            # Check if the cloud is under a roof
            while roof_index < r and current_position >= roof_end:
                roof_start, roof_end = roofs[roof_index]
                roof_index += 1

            if current_position >= roof_start and current_position < roof_end:
                # If the cloud is under a roof, reduce the rain amount by the amount that falls on the roof
                rain_amount -= (roof_end - current_position) * rain_amount / (d - roof_start)

            # Add the rain amount to the total minimum rain
            min_rain += rain_amount

        # Update the current time and position
        current_time = e
        current_position = current_time * 1

    return min_rain

