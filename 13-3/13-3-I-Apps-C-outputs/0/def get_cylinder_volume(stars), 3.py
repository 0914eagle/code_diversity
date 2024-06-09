
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
    volume = pi * radius ** 2 * height

    return volume

def get_min_cylinder_volume(stars):
    # Find the minimum volume cylinder that encloses all the stars
    min_volume = float('inf')
    for i in range(len(stars)):
        for j in range(i+1, len(stars)):
            for k in range(j+1, len(stars)):
                star1 = stars[i]
                star2 = stars[j]
                star3 = stars[k]
                if (star1[0] == star2[0] and star1[1] == star2[1] and star1[2] == star2[2]) or (star1[0] == star3[0] and star1[1] == star3[1] and star1[2] == star3[2]) or (star2[0] == star3[0] and star2[1] == star3[1] and star2[2] == star3[2]):
                    continue
                area = abs((star1[0] * (star2[1] - star3[1]) + star2[0] * (star3[1] - star1[1]) + star3[0] * (star1[1] - star2[1])) / 2)
                height = abs(star1[2] * area / (star2[0] * (star1[1] - star3[1]) + star1[0] * (star3[1] - star2[1]) + star3[0] * (star2[1] - star1[1])))
                volume = area * height
                min_volume = min(min_volume, volume)

    return min_volume

def main():
    n = int(input())
    stars = []
    for i in range(n):
        x, y, z = map(int, input().split())
        stars.append([x, y, z])
    print(get_min_cylinder_volume(stars))

if __name__ == '__main__':
    main()

