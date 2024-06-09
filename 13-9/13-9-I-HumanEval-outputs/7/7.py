
from typing import List

def minPath(grid: List[List[int]], k: int) -> List[int]:
    
    # Initialize the grid with the given values
    grid = [[0] + row for row in grid]
    grid.insert(0, [0] * len(grid[0]))
    grid.append([0] * len(grid[0]))

    # Initialize the distance matrix
    distance = [[float('inf')] * (len(grid[0]) - 1) for _ in range(len(grid) - 1)]

    # Initialize the previous matrix
    previous = [[None] * (len(grid[0]) - 1) for _ in range(len(grid) - 1)]

    # Set the starting point
    start = (0, 0)

    # Set the distance of the starting point to 0
    distance[start] = 0

    # Initialize the queue with the starting point
    queue = [start]

    # Loop until the queue is empty
    while queue:
        # Get the current point
        current = queue.pop(0)

        # Check if the current point is the target point
        if current == (len(grid) - 2, len(grid[0]) - 2):
            # Return the path
            path = []
            while current is not None:
                path.append(grid[current[0] + 1][current[1] + 1])
                current = previous[current[0]][current[1]]
            return path[::-1]

        # Get the neighbors of the current point
        neighbors = [(current[0] - 1, current[1]), (current[0] + 1, current[1]), (current[0], current[1] - 1), (current[0], current[1] + 1)]

        # Loop through the neighbors
        for neighbor in neighbors:
            # Check if the neighbor is valid
            if 0 <= neighbor[0] < len(grid) - 1 and 0 <= neighbor[1] < len(grid[0]) - 1:
                # Check if the distance to the neighbor is not infinite
                if distance[neighbor] != float('inf'):
                    # Check if the distance to the neighbor is less than the current distance
                    if distance[current] + 1 < distance[neighbor]:
                        # Update the distance and the previous point
                        distance[neighbor] = distance[current] + 1
                        previous[neighbor[0]][neighbor[1]] = current

                        # Add the neighbor to the queue
                        queue.append(neighbor)

    # If the target point is not reachable, return an empty list
    return []


if __name__ == "__main__":
    grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    k = 3
    result = minPath(grid, k)
    print(result)

    grid = [[5, 9, 3], [4, 1, 6], [7, 8, 2]]
    k = 1
    result = minPath(grid, k)
    print(result)

