
def get_biker_velocity(n, g, distances, angles):
    velocities = []
    for i in range(n):
        velocity = 0
        for j in range(i):
            velocity += (g * math.cos(math.radians(angles[j])) * distances[j])
        velocities.append(velocity)
    return velocities

