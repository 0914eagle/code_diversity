
from math import sqrt, acos

def get_cylinder_volume(stars):
    # Calculate the centroid of the stars
    centroid = [0, 0, 0]
    for star in stars:
        centroid[0] += star[0]
        centroid[1] += star[1]
        centroid[2] += star[2]
    centroid[0] /= len(stars)
    centroid[1] /= len(stars)
    centroid[2] /= len(stars)

    # Calculate the radius of the cylinder
    radius = 0
    for star in stars:
        distance = sqrt((star[0] - centroid[0]) ** 2 + (star[1] - centroid[1]) ** 2 + (star[2] - centroid[2]) ** 2)
        radius = max(radius, distance)

    # Calculate the height of the cylinder
    height = 0
    for star in stars:
        distance = abs(star[2] - centroid[2])
        height = max(height, distance)

    # Calculate the volume of the cylinder
    volume = radius * radius * height * pi

    return volume

