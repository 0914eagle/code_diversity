
def sunlight_hours(buildings):
    # Calculate the total number of hours of sunlight
    total_hours = 0
    for building in buildings:
        # Calculate the angle of sunlight for each building
        angle = building[1] / 180
        # Calculate the number of hours of sunlight for each building
        hours = angle * 24
        # Add the hours to the total
        total_hours += hours
    # Return the total hours of sunlight
    return total_hours

