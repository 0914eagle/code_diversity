
import math

def get_velocity(n, g, distances, angles):
    velocities = []
    for i in range(n):
        velocity = 0
        for j in range(i, n):
            segment_angle = angles[j] * math.pi / 180
            segment_distance = distances[j]
            velocity += g * math.cos(segment_angle) * segment_distance
        velocities.append(velocity)
    return velocities

