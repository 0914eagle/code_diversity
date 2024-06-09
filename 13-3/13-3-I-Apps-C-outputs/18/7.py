
import math

def get_sunlight_hours(buildings):
    # Calculate the total number of hours of sunlight
    total_hours = 0
    for building in buildings:
        # Calculate the angle of sunlight for each building
        angle = building[1] / math.tan(math.radians(180))
        # Calculate the number of hours of sunlight for each building
        hours = angle * 24
        # Add the hours to the total
        total_hours += hours
    
    return total_hours

