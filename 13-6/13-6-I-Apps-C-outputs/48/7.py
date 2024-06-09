
def find_celery(sightings):
    # Sort the sightings by x-coordinate
    sightings.sort(key=lambda x: x[0])

    # Initialize the minimum polygon with all sightings
    polygon = sightings[:]

    # Iterate through the sightings and remove points that are not in the polygon
    for i in range(len(sightings)):
        for j in range(i+1, len(sightings)):
            if not is_inside_polygon(sightings[i], sightings[j], polygon):
                polygon.remove(sightings[j])

    return len(polygon)

def is_inside_polygon(p1, p2, polygon):
    # Check if p1 is inside the polygon
    for i in range(len(polygon)):
        p3 = polygon[i]
        p4 = polygon[(i+1) % len(polygon)]
        if is_inside_triangle(p1, p2, p3, p4):
            return True

    return False

def is_inside_triangle(p1, p2, p3, p4):
    # Check if p1 is inside the triangle p3-p4-p2
    v1 = (p2[0] - p1[0], p2[1] - p1[1])
    v2 = (p3[0] - p1[0], p3[1] - p1[1])
    v3 = (p4[0] - p1[0], p4[1] - p1[1])
    dot1 = v1[0] * v2[1] - v1[1] * v2[0]
    dot2 = v1[0] * v3[1] - v1[1] * v3[0]
    return dot1 > 0 and dot2 > 0

def main():
    n = int(input())
    vertices = []
    for i in range(n):
        x, y = map(int, input().split())
        vertices.append((x, y))
    k = int(input())
    sightings = []
    for i in range(k):
        x, y = map(int, input().split())
        sightings.append((x, y))
    print(find_celery(sightings))

if __name__ == "__main__":
    main()

