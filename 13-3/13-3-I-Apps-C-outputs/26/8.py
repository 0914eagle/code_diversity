
def f1(L, n, points):
    # Initialize a list to store the bending directions
    directions = []
    
    # Iterate through the points and append the bending directions to the list
    for point in points:
        directions.append(point[1])
    
    # Initialize a set to store the positions of the wire that have been bended
    bended_positions = set()
    
    # Iterate through the points and directions
    for i in range(n):
        # Get the current point and direction
        point = points[i][0]
        direction = directions[i]
        
        # Check if the current point has already been bended
        if point in bended_positions:
            return "GHOST"
        
        # Add the current point to the set of bended positions
        bended_positions.add(point)
        
        # Check if the current point is the starting point
        if point == 0:
            # If the direction is clockwise, add the length of the wire to the set of bended positions
            if direction == "C":
                bended_positions.add(L)
            # If the direction is counterclockwise, add 0 to the set of bended positions
            else:
                bended_positions.add(0)
    
    # If the set of bended positions is equal to the set of all positions on the wire, return "SAFE"
    if bended_positions == set(range(L + 1)):
        return "SAFE"
    
    # Otherwise, return "GHOST"
    return "GHOST"

def f2(L, n, points):
    # Initialize a list to store the bending directions
    directions = []
    
    # Iterate through the points and append the bending directions to the list
    for point in points:
        directions.append(point[1])
    
    # Initialize a set to store the positions of the wire that have been bended
    bended_positions = set()
    
    # Iterate through the points and directions
    for i in range(n):
        # Get the current point and direction
        point = points[i][0]
        direction = directions[i]
        
        # Check if the current point has already been bended
        if point in bended_positions:
            return "GHOST"
        
        # Add the current point to the set of bended positions
        bended_positions.add(point)
        
        # Check if the current point is the starting point
        if point == 0:
            # If the direction is clockwise, add the length of the wire to the set of bended positions
            if direction == "C":
                bended_positions.add(L)
            # If the direction is counterclockwise, add 0 to the set of bended positions
            else:
                bended_positions.add(0)
    
    # If the set of bended positions is equal to the set of all positions on the wire, return "SAFE"
    if bended_positions == set(range(L + 1)):
        return "SAFE"
    
    # Otherwise, return "GHOST"
    return "GHOST"

if __name__ == '__main__':
    L, n = map(int, input().split())
    points = []
    for i in range(n):
        point, direction = map(str, input().split())
        points.append((int(point), direction))
    print(f1(L, n, points))
    print(f2(L, n, points))

