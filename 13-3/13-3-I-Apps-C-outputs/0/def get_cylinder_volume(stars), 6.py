
from math import sqrt, acos

def get_cylinder_volume(stars):
    # Calculate the center of mass of the stars
    center_x, center_y, center_z = 0, 0, 0
    for star in stars:
        center_x += star[0]
        center_y += star[1]
        center_z += star[2]
    center_x /= len(stars)
    center_y /= len(stars)
    center_z /= len(stars)

    # Calculate the radius of the cylinder
    radius = 0
    for star in stars:
        dx = star[0] - center_x
        dy = star[1] - center_y
        dz = star[2] - center_z
        radius = max(radius, sqrt(dx**2 + dy**2 + dz**2))

    # Calculate the height of the cylinder
    height = 0
    for star in stars:
        dy = star[1] - center_y
        dz = star[2] - center_z
        height = max(height, abs(dy) + abs(dz))

    # Calculate the volume of the cylinder
    volume = pi * radius ** 2 * height
    return volume

def get_min_cylinder_volume(stars):
    # Find the minimum volume cylinder that encloses all the stars
    min_volume = float('inf')
    for i in range(len(stars)):
        for j in range(i+1, len(stars)):
            for k in range(j+1, len(stars)):
                star1, star2, star3 = stars[i], stars[j], stars[k]
                dx1 = star2[0] - star1[0]
                dy1 = star2[1] - star1[1]
                dz1 = star2[2] - star1[2]
                dx2 = star3[0] - star1[0]
                dy2 = star3[1] - star1[1]
                dz2 = star3[2] - star1[2]
                dx3 = star3[0] - star2[0]
                dy3 = star3[1] - star2[1]
                dz3 = star3[2] - star2[2]
                volume = abs((dx1 * (dy2 * dz3 - dy3 * dz2) +
                              dx2 * (dy3 * dz1 - dy1 * dz3) +
                              dx3 * (dy1 * dz2 - dy2 * dz1)) / 6)
                min_volume = min(min_volume, volume)
    return min_volume

def solve(stars):
    # Calculate the volume of the cylinder that encloses all the stars
    volume = get_cylinder_volume(stars)

    # Find the minimum volume cylinder that encloses all the stars
    min_volume = get_min_cylinder_volume(stars)

    # Return the ratio of the minimum volume to the total volume
    return min_volume / volume

