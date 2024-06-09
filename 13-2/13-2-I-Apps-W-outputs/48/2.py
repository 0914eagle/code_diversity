
import math

def solve(n, q, polygon, queries):
    # Initialize the answer array
    answer = []
    
    # Iterate over each query
    for query in queries:
        # If the query is of type 1, rotate the polygon
        if query[0] == 1:
            # Get the indices of the vertices to be pinned
            f, t = query[1], query[2]
            
            # Rotate the polygon around the vertex f
            rotate_polygon(polygon, f)
            
            # Pin the vertex t to the wall
            pin_vertex(polygon, t)
            
        # If the query is of type 2, return the coordinates of the vertex
        elif query[0] == 2:
            # Get the index of the vertex to return the coordinates of
            v = query[1]
            
            # Return the coordinates of the vertex
            answer.append(polygon[v])
    
    return answer

def rotate_polygon(polygon, f):
    # Get the coordinates of the vertex f
    xf, yf = polygon[f]
    
    # Iterate over each vertex in the polygon
    for i in range(len(polygon)):
        # Get the coordinates of the current vertex
        xi, yi = polygon[i]
        
        # Rotate the vertex around the vertex f
        polygon[i] = (xi - xf, yi - yf)

def pin_vertex(polygon, t):
    # Get the coordinates of the vertex t
    x, y = polygon[t]
    
    # Pin the vertex to the wall
    polygon[t] = (x, 0)

def main():
    # Read the input
    n, q = map(int, input().split())
    polygon = []
    for i in range(n):
        x, y = map(int, input().split())
        polygon.append((x, y))
    queries = []
    for i in range(q):
        queries.append(list(map(int, input().split())))
    
    # Solve the problem
    answer = solve(n, q, polygon, queries)
    
    # Print the answer
    for x, y in answer:
        print(f"{x:.4f} {y:.4f}")

if __name__ == "__main__":
    main()

