
def get_island_count(image):
    # Initialize a 2D array to keep track of visited cells
    visited = [[False for _ in range(len(image[0]))] for _ in range(len(image))]
    
    # Initialize a counter for the number of islands
    island_count = 0
    
    # Loop through each cell in the image
    for row in range(len(image)):
        for col in range(len(image[0])):
            # If the cell is not visited and is land, mark it as visited and increment the island count
            if not visited[row][col] and image[row][col] == "L":
                mark_island(image, visited, row, col, island_count)
                island_count += 1
    
    return island_count

def mark_island(image, visited, row, col, island_count):
    # Base case: if the cell is already visited or is water, return
    if visited[row][col] or image[row][col] == "W":
        return
    
    # Mark the current cell as visited and add it to the island count
    visited[row][col] = True
    island_count += 1
    
    # Recursively mark all adjacent cells as visited and add them to the island count
    if row > 0 and image[row-1][col] == "L":
        mark_island(image, visited, row-1, col, island_count)
    if row < len(image)-1 and image[row+1][col] == "L":
        mark_island(image, visited, row+1, col, island_count)
    if col > 0 and image[row][col-1] == "L":
        mark_island(image, visited, row, col-1, island_count)
    if col < len(image[0])-1 and image[row][col+1] == "L":
        mark_island(image, visited, row, col+1, island_count)

def main():
    # Read the input image
    r, c = map(int, input().split())
    image = [input() for _ in range(r)]
    
    # Call the get_island_count function and print the result
    print(get_island_count(image))

if __name__ == '__main__':
    main()

