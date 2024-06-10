
import sys
import math

def get_planet_coordinates(file_path):
    with open(file_path, 'r') as f:
        content = f.readlines()
    num_planets = int(content[0])
    coordinates = []
    for i in range(1, num_planets+1):
        coords = [int(x) for x in content[i].split()]
        coordinates.append(coords)
    return coordinates

def find_min_distance(coordinates):
    num_planets = len(coordinates)
    min_distance = float('inf')
    for i in range(num_planets):
        for j in range(i+1, num_planets):
            distance = math.sqrt(sum([(coordinates[i][k]-coordinates[j][k])**2 for k in range(3)]))
            min_distance = min(min_distance, distance)
    return min_distance

def main():
    coordinates = get_planet_coordinates(sys.argv[1])
    print(find_min_distance(coordinates))

if __name__ == '__main__':
    main()

