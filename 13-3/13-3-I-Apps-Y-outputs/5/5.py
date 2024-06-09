
def get_min_islands(image):
    # Initialize a set to store the positions of land cells
    land_cells = set()
    # Initialize a set to store the positions of water cells
    water_cells = set()
    # Initialize a set to store the positions of cloud cells
    cloud_cells = set()
    # Initialize a dictionary to store the neighbors of each cell
    neighbors = {}

    # Loop through the image and populate the sets and dictionary
    for row in range(len(image)):
        for col in range(len(image[row])):
            if image[row][col] == "L":
                land_cells.add((row, col))
            elif image[row][col] == "W":
                water_cells.add((row, col))
            elif image[row][col] == "C":
                cloud_cells.add((row, col))
            neighbors[(row, col)] = []
            if row > 0:
                neighbors[(row, col)].append((row - 1, col))
            if row < len(image) - 1:
                neighbors[(row, col)].append((row + 1, col))
            if col > 0:
                neighbors[(row, col)].append((row, col - 1))
            if col < len(image[row]) - 1:
                neighbors[(row, col)].append((row, col + 1))

    # Initialize a set to store the positions of cells that are part of an island
    island_cells = set()
    # Loop through the land cells and find the cells that are part of an island
    for cell in land_cells:
        if cell not in island_cells:
            dfs(cell, island_cells, neighbors)

    # Return the number of islands
    return len(island_cells)

def dfs(cell, visited, neighbors):
    # Mark the current cell as visited
    visited.add(cell)
    # Recursively explore the neighbors of the current cell
    for neighbor in neighbors[cell]:
        if neighbor not in visited:
            dfs(neighbor, visited, neighbors)

if __name__ == '__main__':
    image = [
        ['L', 'L', 'L', 'L', 'L'],
        ['L', 'L', 'L', 'L', 'L'],
        ['L', 'L', 'L', 'L', 'L'],
        ['L', 'L', 'L', 'L', 'L']
    ]
    print(get_min_islands(image))

