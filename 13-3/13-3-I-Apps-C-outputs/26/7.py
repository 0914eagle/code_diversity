
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
    
    # Check if the list of bends is empty, if it is, return "SAFE"
    if not bends:
        return "SAFE"
    
    # Otherwise, return "GHOST"
    return "GHOST"

def f2(L, n, points):
    # Initialize a set to store the bends
    bends = set()
    
    # Iterate through the points and directions
    for point, direction in points:
        # If the direction is clockwise, add the point to the set of bends
        if direction == "C":
            bends.add(point)
        # If the direction is counterclockwise, remove the point from the set of bends
        else:
            bends.remove(point)
    
    # Check if the set of bends is empty, if it is, return "SAFE"
    if not bends:
        return "SAFE"
    
    # Otherwise, return "GHOST"
    return "GHOST"

if __name__ == '__main__':
    L, n = map(int, input().split())
    points = [tuple(map(int, input().split())) for _ in range(n)]
    print(f1(L, n, points))
    print(f2(L, n, points))

