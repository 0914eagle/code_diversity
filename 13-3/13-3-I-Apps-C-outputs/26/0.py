
def f1(L, n):
    # Initialize a list to store the points and directions
    points = []
    
    # Iterate through the input points and directions
    for i in range(n):
        # Split the input into the point and direction
        point, direction = input().split()
        
        # Convert the point to an integer and the direction to a boolean
        point = int(point)
        direction = direction == "C"
        
        # Add the point and direction to the list
        points.append((point, direction))
    
    # Initialize a set to store the points that have been visited
    visited = set()
    
    # Iterate through the points and directions
    for point, direction in points:
        # If the point has already been visited and the direction is clockwise, return GHOST
        if point in visited and direction:
            return "GHOST"
        
        # Add the point to the set of visited points
        visited.add(point)
    
    # If the wire does not touch itself, return SAFE
    return "SAFE"

def f2(...):
    # Implement f2 here
    pass

if __name__ == '__main__':
    L, n = map(int, input().split())
    print(f1(L, n))

