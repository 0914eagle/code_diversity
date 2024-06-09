
import math

def get_sunlight_hours(buildings):
    # Calculate the total width of the avenue
    total_width = sum([building[1] for building in buildings])
    
    # Calculate the angle of sunlight for each building
    sunlight_angles = []
    for building in buildings:
        angle = building[1] / total_width * 180
        sunlight_angles.append(angle)
    
    # Calculate the hours of sunlight for each building
    sunlight_hours = []
    for angle in sunlight_angles:
        hours = angle / 360 * 24
        sunlight_hours.append(hours)
    
    return sunlight_hours

