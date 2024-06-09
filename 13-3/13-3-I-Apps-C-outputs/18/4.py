
def get_sunlight_hours(buildings):
    # Calculate the total number of hours of sunlight
    total_hours = 0
    for building in buildings:
        # Calculate the angle of sunlight for each building
        angle = (building[1] / 180) * 360
        # Add the angle to the total hours
        total_hours += angle
    return total_hours

