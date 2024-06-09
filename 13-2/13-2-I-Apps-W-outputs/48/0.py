
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
            
        # If the query is of type 2, find the coordinates of the vertex
        elif query[0] == 2:
            # Get the index of the vertex to find the coordinates of
            v = query[1]
            
            # Find the coordinates of the vertex
            x, y = polygon[v - 1]
            
            # Add the coordinates to the answer array
            answer.append([x, y])
    
    return answer

def rotate_polygon(polygon, f):
    # Get the indices of the vertices to be rotated
    vertices = [i for i in range(len(polygon)) if i != f - 1]
    
    # Rotate the polygon around the vertex f
    for i in vertices:
        polygon[i] = [polygon[i][0] - polygon[f - 1][0], polygon[i][1] - polygon[f - 1][1]]

def pin_vertex(polygon, t):
    # Get the index of the vertex to be pinned
    t = t - 1
    
    # Pin the vertex to the wall
    polygon[t] = [0, 0]

def main():
    # Read the input
    n, q = map(int, input().split())
    polygon = []
    for i in range(n):
        x, y = map(int, input().split())
        polygon.append([x, y])
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

