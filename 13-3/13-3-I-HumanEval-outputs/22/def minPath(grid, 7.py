
from typing import List

def minPath(grid: List[List[int]], k: int) -> List[int]:
    
    # Initialize the grid with the given values
    grid = [[0] + row + [0] for row in grid]
    grid.insert(0, [0] * len(grid[0]))
    grid.append([0] * len(grid[0]))

    # Initialize the minimum path with the first cell
    min_path = [grid[1][1]]

    # Loop through the cells of the grid
    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[0]) - 1):
            # If the current cell is not part of the minimum path, skip it
            if grid[i][j] == 0:
                continue

            # If the current cell is the last cell of the minimum path, add it to the path
            if len(min_path) == k:
                min_path.append(grid[i][j])
                break

            # If the current cell is not the last cell of the minimum path, try to extend the path
            for neighbor in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                # If the neighbor cell is not part of the minimum path, skip it
                if grid[neighbor[0]][neighbor[1]] == 0:
                    continue

                # If the neighbor cell is the last cell of the minimum path, add it to the path
                if len(min_path) + 1 == k:
                    min_path.append(grid[neighbor[0]][neighbor[1]])
                    break

                # If the neighbor cell is not the last cell of the minimum path, try to extend the path
                for next_neighbor in [(neighbor[0] - 1, neighbor[1]), (neighbor[0] + 1, neighbor[1]), (neighbor[0], neighbor[1] - 1), (neighbor[0], neighbor[1] + 1)]:
                    # If the next neighbor cell is not part of the minimum path, skip it
                    if grid[next_neighbor[0]][next_neighbor[1]] == 0:
                        continue

                    # If the next neighbor cell is the last cell of the minimum path, add it to the path
                    if len(min_path) + 2 == k:
                        min_path.append(grid[next_neighbor[0]][next_neighbor[1]])
                        break

                    # If the next neighbor cell is not the last cell of the minimum path, try to extend the path
                    for final_neighbor in [(next_neighbor[0] - 1, next_neighbor[1]), (next_neighbor[0] + 1, next_neighbor[1]), (next_neighbor[0], next_neighbor[1] - 1), (next_neighbor[0], next_neighbor[1] + 1)]:
                        # If the final neighbor cell is not part of the minimum path, skip it
                        if grid[final_neighbor[0]][final_neighbor[1]] == 0:
                            continue

                        # If the final neighbor cell is the last cell of the minimum path, add it to the path
                        if len(min_path) + 3 == k:
                            min_path.append(grid[final_neighbor[0]][final_neighbor[1]])
                            break

    # Return the minimum path
    return min_path

