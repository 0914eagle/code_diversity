
def get_min_rain_amount(d, t, c, r, clouds, roofs):
    # Initialize variables
    min_rain_amount = 0
    current_time = 0
    current_location = 0
    current_rain = 0
    roof_segments = []

    # Sort the clouds by their start time
    clouds.sort(key=lambda x: x[0])

    # Add the roof segments to a list
    for i in range(r):
        roof_segments.append(roofs[i])

    # Loop through the clouds and calculate the min rain amount
    for cloud in clouds:
        start_time, end_time, probability, rain_amount = cloud
        current_time = max(current_time, start_time)
        current_location = current_time * 1
        current_rain = current_rain + probability * rain_amount * (end_time - current_time)
        min_rain_amount = max(min_rain_amount, current_rain)
        current_time = end_time

    # Loop through the roof segments and calculate the min rain amount
    for segment in roof_segments:
        start_location, end_location = segment
        current_location = max(current_location, start_location)
        current_rain = current_rain + (end_location - current_location) * 1
        min_rain_amount = max(min_rain_amount, current_rain)
        current_location = end_location

    return min_rain_amount

