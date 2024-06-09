
def solve(start, end, charge):
    # Initialize a set to store the visited intersections
    visited = set()
    # Initialize a queue to store the intersections to be visited
    queue = [start]
    # Loop until the queue is empty
    while queue:
        # Get the current intersection from the queue
        intersection = queue.pop(0)
        # If the current intersection is the destination, return True
        if intersection == end:
            return True
        # If the current intersection has not been visited before, mark it as visited and add it to the queue
        if intersection not in visited:
            visited.add(intersection)
            queue.extend(get_neighbors(intersection))
        # If the current intersection has been visited before, continue to the next intersection
        else:
            continue
    # If the queue is empty and the destination has not been reached, return False
    return False

# Function to get the neighbors of an intersection
def get_neighbors(intersection):
    # Get the x and y coordinates of the intersection
    x, y = intersection
    # Initialize a list to store the neighbors
    neighbors = []
    # Add the left, right, straight, and U-turn moves to the list of neighbors
    neighbors.append((x, y-1))
    neighbors.append((x, y+1))
    neighbors.append((x-1, y))
    neighbors.append((x+1, y))
    return neighbors

