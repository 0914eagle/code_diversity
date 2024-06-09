
import math

def get_sunlight_hours(buildings):
    # Calculate the total number of hours of sunlight
    total_hours = 0
    for building in buildings:
        # Calculate the angle of sunlight for each building
        angle = building[1] / 2.0
        # Calculate the number of hours of sunlight for each building
        hours = 180.0 * angle / 360.0
        total_hours += hours
    
    return total_hours

