
import math

def get_sunlight_hours(buildings):
    # Calculate the total width of the avenue
    total_width = sum([building[1] for building in buildings])
    
    # Calculate the angle of sunlight for each building
    angles = []
    for building in buildings:
        angle = building[1] / total_width * 180
        angles.append(angle)
    
    # Calculate the hours of sunlight for each building
    hours = []
    for angle in angles:
        hours.append(angle / 360 * 24)
    
    return hours

