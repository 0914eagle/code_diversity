
import math

def get_velocity(n, g, distances, angles):
    velocities = []
    for i in range(n):
        velocity = 0
        for j in range(i, n):
            velocity += math.cos(math.radians(angles[j])) * g * distances[j]
        velocities.append(velocity)
    return velocities

