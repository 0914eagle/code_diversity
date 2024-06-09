
def find_min_path_sum(grid):
    # Initialize the minimum path sum to infinity
    min_path_sum = float('inf')
    # Initialize the current position as the top-left cell
    current_position = (0, 0)
    # Initialize the current path sum to the value at the current position
    current_path_sum = grid[current_position[0]][current_position[1]]
    # Initialize a set to store the visited cells
    visited = set()
    # Initialize a queue to store the cells to be visited
    queue = [(current_position, current_path_sum)]
    # Loop until the queue is empty
    while queue:
        # Get the current cell and path sum from the queue
        current_position, current_path_sum = queue.pop(0)
        # If the current cell is the bottom-right cell, update the minimum path sum
        if current_position == (len(grid) - 1, len(grid[0]) - 1):
            min_path_sum = min(min_path_sum, current_path_sum)
            continue
        # Get the neighbors of the current cell
        neighbors = get_neighbors(grid, current_position)
        # Loop through the neighbors
        for neighbor in neighbors:
            # If the neighbor has not been visited, mark it as visited and add it to the queue
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, current_path_sum + grid[neighbor[0]][neighbor[1]]))
    # Return the minimum path sum
    return min_path_sum

def get_neighbors(grid, position):
    # Get the row and column of the current cell
    row, col = position
    # Get the neighbors of the current cell
    neighbors = [(row + 1, col), (row, col + 1)]
    # Filter the neighbors that are out of bounds
    neighbors = [neighbor for neighbor in neighbors if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0])]
    return neighbors

if __name__ == '__main__':
    grid = [[1,3,1],
            [1,5,1],
            [4,2,1]]
    print(find_min_path_sum(grid))

