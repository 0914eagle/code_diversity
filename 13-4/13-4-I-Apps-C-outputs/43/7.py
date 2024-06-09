
def solve(A, B):
    # Find the minimum cost to cut B out of A
    cost = 0
    
    # While B is not completely inside A
    while not is_inside(A, B):
        # Find the edge of A that is closest to an edge of B
        closest_edge = find_closest_edge(A, B)
        
        # Cut A along the closest edge
        A = cut(A, closest_edge)
        
        # Update the cost
        cost += length(closest_edge)
    
    return cost

def is_inside(A, B):
    # Check if all vertices of B are inside A
    for vertex in B:
        if not is_inside_polygon(A, vertex):
            return False
    return True

def find_closest_edge(A, B):
    # Find the edge of A that is closest to an edge of B
    closest_edge = None
    min_distance = float('inf')
    for edge in A:
        for vertex in B:
            distance = distance_to_line(edge, vertex)
            if distance < min_distance:
                min_distance = distance
                closest_edge = edge
    return closest_edge

def cut(A, edge):
    # Cut A along the given edge
    v1, v2 = edge
    v3 = (v1[0] + v2[0], v1[1] + v2[1])
    return [v1, v2, v3]

def length(edge):
    # Return the length of the given edge
    v1, v2 = edge
    return ((v1[0] - v2[0]) ** 2 + (v1[1] - v2[1]) ** 2) ** 0.5

def distance_to_line(edge, point):
    # Return the distance from the point to the line defined by the edge
    v1, v2 = edge
    x1, y1 = point
    x2, y2 = v1
    x3, y3 = v2
    num = (y3 - y2) * x1 - (x3 - x2) * y1 + x3 * y2 - y3 * x2
    den = ((y3 - y2) ** 2 + (x3 - x2) ** 2) ** 0.5
    return num / den

def is_inside_polygon(polygon, point):
    # Check if the point is inside the polygon
    x, y = point
    inside = False
    for i in range(len(polygon)):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i + 1) % len(polygon)]
        if y1 < y:
            if y2 >= y:
                if is_left(x1, y1, x2, y2, x, y) > 0:
                    inside = not inside
        elif y2 < y:
            if is_left(x1, y1, x2, y2, x, y) < 0:
                inside = not inside
    return inside

def is_left(x1, y1, x2, y2, x3, y3):
    # Check if a point is to the left of a line
    return (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)

