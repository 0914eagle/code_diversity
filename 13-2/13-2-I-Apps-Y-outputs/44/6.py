
def solve(start, end, battery):
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
            return "Y"
        # If the current intersection has not been visited before, mark it as visited and add it to the queue
        if intersection not in visited:
            visited.add(intersection)
            # Get the x and y coordinates of the current intersection
            x, y = intersection
            # Get the possible moves from the current intersection
            moves = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
            # Filter the moves to only include valid intersections
            moves = [move for move in moves if -1000 <= move[0] <= 1000 and -1000 <= move[1] <= 1000]
            # Add the filtered moves to the queue
            queue.extend(moves)
    # If the queue is empty and the destination has not been reached, return False
    return "N"

