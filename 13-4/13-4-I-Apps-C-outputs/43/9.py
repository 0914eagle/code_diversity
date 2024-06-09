
def solve(A, B):
    # Find the minimum cost to cut B out of A
    cost = 0
    
    # While B is not completely inside A
    while not is_inside(A, B):
        # Find the edge of A that is closest to an edge of B
        closest_edge = find_closest_edge(A, B)
        
        # Cut along the closest edge
        A, B = cut(A, B, closest_edge)
        
        # Add the length of the cut to the cost
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

def cut(A, B, edge):
    # Cut A along the given edge and return the two resulting polygons
    A1 = []
    A2 = []
    for vertex in A:
        if is_left(edge, vertex) > 0:
            A1.append(vertex)
        else:
            A2.append(vertex)
    return A1, A2

def is_left(edge, vertex):
    # Check if a vertex is left of an edge
    return (vertex[0] - edge[0][0]) * (edge[1][1] - edge[0][1]) - (vertex[1] - edge[0][1]) * (edge[1][0] - edge[0][0])

def distance_to_line(edge, vertex):
    # Find the distance from a vertex to a line
    a = edge[1][1] - edge[0][1]
    b = edge[0][0] - edge[1][0]
    c = -a * edge[0][0] - b * edge[0][1]
    return abs(a * vertex[0] + b * vertex[1] + c) / math.sqrt(a**2 + b**2)

def length(edge):
    # Find the length of an edge
    return math.sqrt((edge[1][0] - edge[0][0])**2 + (edge[1][1] - edge[0][1])**2)

def is_inside_polygon(polygon, vertex):
    # Check if a vertex is inside a polygon
    x, y = vertex
    inside = False
    j = len(polygon) - 1
    for i in range(len(polygon)):
        xi, yi = polygon[i]
        xj, yj = polygon[j]
        intersect = ((yi > y) != (yj > y)) and (x < (xj - xi) * (y - yi) / (yj - yi) + xi)
        if intersect:
            inside = not inside
        j = i
    return inside

