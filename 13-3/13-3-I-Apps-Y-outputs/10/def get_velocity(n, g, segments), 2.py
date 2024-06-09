
import math

def get_velocity(n, g, segments):
    velocities = []
    for i in range(n):
        distance, angle = segments[i]
        velocity = math.sqrt(2 * g * distance * math.cos(math.radians(angle)))
        velocities.append(velocity)
    return velocities

