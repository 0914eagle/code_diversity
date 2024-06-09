
def f1(L, n, points):
    # Initialize a list to store the bends
    bends = []
    
    # Iterate through the points and directions
    for point, direction in points:
        # If the direction is clockwise, add the point to the list of bends
        if direction == "C":
            bends.append(point)
        # If the direction is counterclockwise, remove the point from the list of bends
        else:
            bends.remove(point)
    
    # Check if the list of bends is empty, if so, return "SAFE"
    if not bends:
        return "SAFE"
    
    # Initialize a set to store the positions of the bends
    bend_positions = set()
    
    # Iterate through the bends and add their positions to the set
    for bend in bends:
        bend_positions.add(bend)
    
    # Check if the set of bend positions contains any duplicates, if so, return "GHOST"
    if len(bend_positions) != len(bends):
        return "GHOST"
    
    # If the list of bends is empty and there are no duplicates in the set of bend positions, return "SAFE"
    return "SAFE"

def f2(L, n, points):
    # Initialize a list to store the bends
    bends = []
    
    # Iterate through the points and directions
    for point, direction in points:
        # If the direction is clockwise, add the point to the list of bends
        if direction == "C":
            bends.append(point)
        # If the direction is counterclockwise, remove the point from the list of bends
        else:
            bends.remove(point)
    
    # Check if the list of bends is empty, if so, return "SAFE"
    if not bends:
        return "SAFE"
    
    # Initialize a set to store the positions of the bends
    bend_positions = set()
    
    # Iterate through the bends and add their positions to the set
    for bend in bends:
        bend_positions.add(bend)
    
    # Check if the set of bend positions contains any duplicates, if so, return "GHOST"
    if len(bend_positions) != len(bends):
        return "GHOST"
    
    # If the list of bends is empty and there are no duplicates in the set of bend positions, return "SAFE"
    return "SAFE"

if __name__ == '__main__':
    L, n = map(int, input().split())
    points = []
    for _ in range(n):
        point, direction = input().split()
        points.append((int(point), direction))
    print(f1(L, n, points))

