
def solve(n, q, polygon, queries):
    # Initialize the answer array
    answer = []
    
    # Iterate over each query
    for query in queries:
        # If the query is of type 1, rotate the polygon
        if query[0] == 1:
            # Get the indices of the vertices to be pinned
            f = query[1]
            t = query[2]
            
            # Rotate the polygon
            rotate_polygon(polygon, f, t)
        
        # If the query is of type 2, get the coordinates of the vertex
        elif query[0] == 2:
            # Get the index of the vertex
            v = query[1]
            
            # Get the coordinates of the vertex
            x, y = polygon[v]
            
            # Add the coordinates to the answer array
            answer.append([x, y])
    
    return answer

def rotate_polygon(polygon, f, t):
    # Get the indices of the vertices to be pinned
    f = f - 1
    t = t - 1
    
    # Get the coordinates of the vertices to be pinned
    x1, y1 = polygon[f]
    x2, y2 = polygon[t]
    
    # Calculate the angle of rotation
    angle = np.arctan2(y2 - y1, x2 - x1)
    
    # Rotate the polygon
    for i in range(len(polygon)):
        x, y = polygon[i]
        x_new = x * np.cos(angle) - y * np.sin(angle)
        y_new = x * np.sin(angle) + y * np.cos(angle)
        polygon[i] = [x_new, y_new]

