
import math

def get_distances(planets):
    distances = []
    for i in range(len(planets)):
        for j in range(i+1, len(planets)):
            distance = math.sqrt(sum([(planets[i][k] - planets[j][k])**2 for k in range(3)]))
            distances.append(distance)
    return distances

def get_min_distance(planets):
    distances = get_distances(planets)
    min_distance = sum(distances)
    for i in range(len(planets)):
        for j in range(i+1, len(planets)):
            distance = distances[i*len(planets) + j] + distances[(i+1)*len(planets) + j+1]
            if distance < min_distance:
                min_distance = distance
    return min_distance

def main():
    num_planets = int(input())
    planets = []
    for i in range(num_planets):
        planets.append([int(x) for x in input().split()])
    print(get_min_distance(planets))

if __name__ == '__main__':
    main()

