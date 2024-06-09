
import math

def get_angle(x1, y1, x2, y2):
    # Calculate the dot product of the two vectors
    dot_product = x1 * x2 + y1 * y2

    # Calculate the magnitude of the two vectors
    magnitude_1 = math.sqrt(x1 ** 2 + y1 ** 2)
    magnitude_2 = math.sqrt(x2 ** 2 + y2 ** 2)

    # Calculate the cosine of the angle between the vectors
    cosine_angle = dot_product / (magnitude_1 * magnitude_2)

    # Calculate the angle in radians
    angle = math.acos(cosine_angle)

    # Convert the angle to degrees
    angle = math.degrees(angle)

    return angle

def main():
    # Read the number of points from stdin
    n = int(input())

    # Read the coordinates of the points from stdin
    points = []
    for i in range(n):
        x, y = map(float, input().split())
        points.append((x, y))

    # Calculate the angle between the vectors
    angle = get_angle(points[0][0], points[0][1], points[1][0], points[1][1])

    # Print the angle to stdout
    print(angle)

if __name__ == "__main__":
    main()

