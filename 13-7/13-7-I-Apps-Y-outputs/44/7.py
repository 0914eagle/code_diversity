
import math

def get_min_rod_length(triangles):
    # Calculate the minimum rod length by finding the maximum distance between the centroids of any two triangles
    centroids = []
    for triangle in triangles:
        centroids.append(get_centroid(triangle))
    max_distance = 0
    for i in range(len(centroids)):
        for j in range(i+1, len(centroids)):
            distance = math.sqrt(math.pow(centroids[i][0] - centroids[j][0], 2) + math.pow(centroids[i][1] - centroids[j][1], 2))
            max_distance = max(max_distance, distance)
    return max_distance

def get_centroid(triangle):
    # Calculate the centroid of a triangle
    x1, y1 = triangle[0]
    x2, y2 = triangle[1]
    x3, y3 = triangle[2]
    centroid_x = (x1 + x2 + x3) / 3
    centroid_y = (y1 + y2 + y3) / 3
    return (centroid_x, centroid_y)

def main():
    triangles = []
    for _ in range(int(input())):
        triangles.append([tuple(map(int, input().split())) for _ in range(3)])
    print(get_min_rod_length(triangles))

if __name__ == "__main__":
    main()

