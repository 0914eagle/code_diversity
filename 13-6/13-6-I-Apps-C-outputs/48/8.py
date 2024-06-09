
def find_smallest_polygon(sightings):
    # Sort the sightings in clockwise order
    sorted_sightings = sorted(sightings, key=lambda x: x[0])

    # Initialize the smallest polygon with the first sighting
    smallest_polygon = [sorted_sightings[0]]

    # Iterate through the remaining sightings
    for sighting in sorted_sightings[1:]:
        # If the current sighting is inside the smallest polygon, add it to the polygon
        if is_inside_polygon(smallest_polygon, sighting):
            smallest_polygon.append(sighting)
        # If the current sighting is not inside the smallest polygon, create a new polygon with the current sighting
        else:
            smallest_polygon = [sighting]

    return len(smallest_polygon)

def is_inside_polygon(polygon, point):
    # Get the vertices of the polygon
    vertices = [(point[0], point[1]) for point in polygon]

    # Get the area of the polygon
    area = get_polygon_area(vertices)

    # Get the area of the triangle created by the point and the two adjacent vertices
    triangle_area = get_triangle_area(point, vertices[0], vertices[1])

    # If the area of the triangle is less than the area of the polygon, the point is inside the polygon
    return triangle_area < area

def get_polygon_area(vertices):
    # Get the area of the polygon
    area = 0
    for i in range(len(vertices)):
        area += (vertices[i][0] * vertices[(i+1)%len(vertices)][1]) - (vertices[i][1] * vertices[(i+1)%len(vertices)][0])
    return abs(area / 2)

def get_triangle_area(point, vertex1, vertex2):
    # Get the area of the triangle
    area = (point[0] * (vertex1[1] - vertex2[1])) + (point[1] * (vertex2[0] - vertex1[0])) + (vertex1[0] * vertex2[1]) - (vertex1[1] * vertex2[0])
    return abs(area / 2)

def main():
    # Read the input
    num_vertices = int(input())
    vertices = []
    for i in range(num_vertices):
        x, y = map(int, input().split())
        vertices.append((x, y))
    num_sightings = int(input())
    sightings = []
    for i in range(num_sightings):
        x, y = map(int, input().split())
        sightings.append((x, y))

    # Find the smallest polygon
    smallest_polygon = find_smallest_polygon(sightings)

    # Print the result
    print(smallest_polygon)

if __name__ == "__main__":
    main()

