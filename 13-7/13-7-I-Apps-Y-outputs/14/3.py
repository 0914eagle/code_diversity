
import math

def find_distance(A, B, H, M):
    # Calculate the angle made by the hour hand
    hour_angle = (30 * H) % 360
    
    # Calculate the angle made by the minute hand
    minute_angle = (6 * M) % 360
    
    # Calculate the angle between the hour and minute hands
    angle_between_hands = abs(hour_angle - minute_angle)
    
    # Calculate the distance between the hands
    distance = math.sin(math.radians(angle_between_hands)) * A
    
    return distance
