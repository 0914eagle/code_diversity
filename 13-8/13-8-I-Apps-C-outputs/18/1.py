
def get_min_rain(d, t, c, r, clouds, roofs):
    # Initialize variables
    min_rain = 0
    current_time = 0
    current_position = 0
    roof_index = 0

    # Loop through the clouds
    for i in range(c):
        cloud = clouds[i]
        s, e, p, a = cloud
        cloud_duration = e - s

        # Check if the cloud is in the zip code
        if p > 0:
            # Check if the cloud is currently raining
            if current_time >= s and current_time < e:
                # Calculate the rain amount for the current cloud
                rain_amount = a * (min(e, current_time + t) - max(s, current_time))
                min_rain += rain_amount

        # Move to the next cloud
        current_time += cloud_duration

    # Loop through the roofs
    for i in range(r):
        roof = roofs[i]
        x, y = roof

        # Check if the current position is within the roof segment
        if current_position >= x and current_position < y:
            # Calculate the time until the roof ends
            time_until_end = y - current_position

            # Check if the time until the roof ends is less than the time until the bus leaves
            if time_until_end < t:
                # Calculate the rain amount for the current roof segment
                rain_amount = min_rain * (time_until_end / t)
                min_rain -= rain_amount

                # Move to the next roof segment
                current_position = y
                roof_index += 1

                # Check if there are no more roofs
                if roof_index == r:
                    break

                # Get the next roof segment
                next_roof = roofs[roof_index]
                x_next, y_next = next_roof

                # Calculate the time until the next roof starts
                time_until_next = x_next - current_position

                # Check if the time until the next roof starts is less than the time until the bus leaves
                if time_until_next < t:
                    # Calculate the rain amount for the current roof segment
                    rain_amount = min_rain * (time_until_next / t)
                    min_rain -= rain_amount

                    # Move to the next roof segment
                    current_position = x_next
                    roof_index += 1

    return min_rain

