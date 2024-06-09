
def get_island_count(image):
    # Initialize a 2D array to store the number of islands visited
    visited = [[0 for _ in range(len(image[0]))] for _ in range(len(image))]
    
    # Initialize a queue to store the coordinates of the cells to be visited
    queue = []
    
    # Initialize the island count
    island_count = 0
    
    # Loop through each row of the image
    for i in range(len(image)):
        # Loop through each column of the image
        for j in range(len(image[0])):
            # If the current cell is land and has not been visited before, visit it and its neighbors
            if image[i][j] == "L" and visited[i][j] == 0:
                # Increment the island count
                island_count += 1
                
                # Add the current cell to the queue
                queue.append((i, j))
                
                # Loop until the queue is empty
                while queue:
                    # Get the coordinates of the cell to be visited
                    x, y = queue.pop(0)
                    
                    # Visit the current cell and its neighbors
                    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        # Get the coordinates of the neighboring cell
                        nx, ny = x + dx, y + dy
                        
                        # If the neighboring cell is land and has not been visited before, visit it and add it to the queue
                        if 0 <= nx < len(image) and 0 <= ny < len(image[0]) and image[nx][ny] == "L" and visited[nx][ny] == 0:
                            visited[nx][ny] = 1
                            queue.append((nx, ny))
    
    # Return the island count
    return island_count

def main():
    # Read the input
    r, c = map(int, input().split())
    image = [input() for _ in range(r)]
    
    # Get the island count
    island_count = get_island_count(image)
    
    # Print the island count
    print(island_count)

if __name__ == '__main__':
    main()

