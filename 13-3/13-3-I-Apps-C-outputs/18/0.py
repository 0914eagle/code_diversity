
import math

def get_sunlight_hours(buildings):
    # Calculate the total number of hours of sunlight
    total_hours = 0
    for building in buildings:
        # Calculate the angle of sunlight for each building
        angle = building[1] / math.tan(math.radians(180))
        # Add the hours of sunlight for each building to the total
        total_hours += angle
    return total_hours

