
from math import sqrt, acos

def get_cylinder_volume(stars):
    # Calculate the center of mass of the stars
    center_x = sum([star[0] for star in stars]) / len(stars)
    center_y = sum([star[1] for star in stars]) / len(stars)
    center_z = sum([star[2] for star in stars]) / len(stars)

    # Calculate the distance of each star from the center of mass
    distances = []
    for star in stars:
        distances.append(sqrt((star[0] - center_x) ** 2 + (star[1] - center_y) ** 2 + (star[2] - center_z) ** 2))

    # Calculate the maximum distance of a star from the center of mass
    max_distance = max(distances)

    # Calculate the radius of the cylinder
    radius = sqrt(max_distance ** 2 - (distances[0] - max_distance) ** 2)

    # Calculate the height of the cylinder
    height = 2 * max_distance

    # Calculate the volume of the cylinder
    volume = pi * radius ** 2 * height

    return volume

