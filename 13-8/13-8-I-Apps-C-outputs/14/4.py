
import math

def get_centre(points):
    # Calculate the centroid of the points
    centroid = [0, 0, 0]
    for point in points:
        centroid[0] += point[0]
        centroid[1] += point[1]
        centroid[2] += point[2]
    centroid[0] /= len(points)
    centroid[1] /= len(points)
    centroid[2] /= len(points)

    # Calculate the distance of each point from the centroid
    distances = []
    for point in points:
        distance = math.sqrt((point[0] - centroid[0]) ** 2 + (point[1] - centroid[1]) ** 2 + (point[2] - centroid[2]) ** 2)
        distances.append(distance)

    # Find the point with the maximum distance from the centroid
    max_distance = max(distances)
    max_distance_index = distances.index(max_distance)

    # Return the coordinates of the point with the maximum distance from the centroid
    return points[max_distance_index]

def main():
    points = []
    for _ in range(4):
        x, y, z = map(float, input().split())
        points.append([x, y, z])
    centre = get_centre(points)
    print(" ".join(str(round(x, 4)) for x in centre))

if __name__ == '__main__':
    main()

