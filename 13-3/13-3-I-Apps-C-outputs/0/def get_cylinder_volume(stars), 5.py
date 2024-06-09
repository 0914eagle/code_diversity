
from math import sqrt, acos

def get_cylinder_volume(stars):
    # Calculate the center of mass of the stars
    center_x = sum([star[0] for star in stars]) / len(stars)
    center_y = sum([star[1] for star in stars]) / len(stars)
    center_z = sum([star[2] for star in stars]) / len(stars)

    # Calculate the radius of the cylinder
    radius = sqrt(max([(star[0] - center_x) ** 2 + (star[1] - center_y) ** 2 + (star[2] - center_z) ** 2 for star in stars]))

    # Calculate the height of the cylinder
    height = max([star[2] for star in stars]) - min([star[2] for star in stars])

    # Calculate the volume of the cylinder
    volume = 2 * pi * radius * height

    return volume

def get_smallest_cylinder_volume(stars):
    # Find the smallest possible volume cylinder that encloses all the stars
    smallest_volume = float('inf')
    for i in range(len(stars)):
        for j in range(i+1, len(stars)):
            for k in range(j+1, len(stars)):
                # Check if the three stars form a triangle
                if (stars[i][0] - stars[j][0]) * (stars[k][1] - stars[j][1]) != (stars[i][1] - stars[j][1]) * (stars[k][0] - stars[j][0]):
                    continue

                # Calculate the area of the triangle
                area = 0.5 * abs((stars[i][0] - stars[j][0]) * (stars[k][1] - stars[j][1]) - (stars[i][1] - stars[j][1]) * (stars[k][0] - stars[j][0]))

                # Calculate the height of the cylinder
                height = area / (2 * pi * radius)

                # Calculate the volume of the cylinder
                volume = 2 * pi * radius * height

                # Check if the volume is smaller than the current smallest volume
                if volume < smallest_volume:
                    smallest_volume = volume

    return smallest_volume

if __name__ == '__main__':
    n = int(input())
    stars = []
    for i in range(n):
        x, y, z = map(int, input().split())
        stars.append((x, y, z))
    print(get_smallest_cylinder_volume(stars))

