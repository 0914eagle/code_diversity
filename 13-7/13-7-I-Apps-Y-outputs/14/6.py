
import math

def find_distance(A, B, H, M):
    # Calculate the angle between the hour and minute hands
    angle = (M / 60.0) * 360.0

    # Calculate the distance between the unfixed endpoints of the hands
    distance = abs(A * math.sin(math.radians(angle)) - B * math.sin(math.radians(angle)))

    return distance

