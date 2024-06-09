
import math

def get_sunlight_hours(buildings):
    # Calculate the total number of hours of sunlight
    total_hours = 0
    for building in buildings:
        # Calculate the angle of sunlight for each building
        angle = building[1] / 2
        # Calculate the hours of sunlight for each building
        hours = 2 * math.pi * (1 - math.cos(angle))
        total_hours += hours
    
    return total_hours

