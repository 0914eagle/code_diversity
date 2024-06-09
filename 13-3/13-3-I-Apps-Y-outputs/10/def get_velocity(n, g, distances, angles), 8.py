
import math

def get_velocity(n, g, distances, angles):
    velocities = []
    for i in range(n):
        velocity = 0
        for j in range(i, n):
            segment_length = distances[j] - distances[i]
            segment_angle = angles[j] - angles[i]
            acceleration = g * math.cos(math.radians(segment_angle))
            velocity += acceleration * segment_length
        velocities.append(velocity)
    return velocities

