
def find_min_path_sum(grid):
    # Initialize the minimum path sum to infinity
    min_path_sum = float('inf')
    # Initialize the current position as the top-left corner
    current_position = (0, 0)
    # Initialize the current path sum to the value at the current position
    current_path_sum = grid[current_position[0]][current_position[1]]
    # Initialize a set to store the visited positions
    visited = set()
    # Initialize a queue to store the positions to be visited
    queue = [(current_position, current_path_sum)]
    # Loop until the queue is empty
    while queue:
        # Get the current position and path sum from the queue
        current_position, current_path_sum = queue.pop(0)
        # If the current position is the bottom-right corner, update the minimum path sum
        if current_position == (len(grid) - 1, len(grid[0]) - 1):
            min_path_sum = min(min_path_sum, current_path_sum)
            continue
        # Get the neighbors of the current position
        neighbors = [(current_position[0] + 1, current_position[1]), (current_position[0], current_position[1] + 1)]
        # Loop through the neighbors
        for neighbor in neighbors:
            # If the neighbor is not out of bounds and has not been visited, add it to the queue
            if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]) and neighbor not in visited:
                queue.append((neighbor, current_path_sum + grid[neighbor[0]][neighbor[1]]))
                visited.add(neighbor)
    # Return the minimum path sum
    return min_path_sum

