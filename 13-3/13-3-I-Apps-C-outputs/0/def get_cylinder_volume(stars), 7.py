
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

    # Calculate the maximum distance from the center of mass
    max_distance = max(distances)

    # Calculate the volume of the cylinder
    volume = 2 * 3.14159265359 * max_distance * sum(distances)

    return volume

def get_smallest_cylinder_volume(stars):
    # Find all possible orientations of the cylinder
    orientations = []
    for i in range(len(stars)):
        for j in range(i+1, len(stars)):
            for k in range(j+1, len(stars)):
                orientations.append([stars[i], stars[j], stars[k]])

    # Calculate the volume of each orientation and find the smallest one
    smallest_volume = float('inf')
    for orientation in orientations:
        volume = get_cylinder_volume(orientation)
        if volume < smallest_volume:
            smallest_volume = volume

    return smallest_volume

def main():
    n = int(input())
    stars = []
    for i in range(n):
        x, y, z = map(int, input().split())
        stars.append([x, y, z])
    print(get_smallest_cylinder_volume(stars))

if __name__ == "__main__":
    main()

