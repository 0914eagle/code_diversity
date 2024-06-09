
import math

def get_velocity(segments, g):
    velocities = []
    for segment in segments:
        distance, angle = segment
        velocity = math.sqrt(2 * g * distance * math.cos(math.radians(angle)))
        velocities.append(velocity)
    return velocities

