
def is_valid_island(image, row, col, visited):
    # Check if the current position is valid
    if row < 0 or row >= len(image) or col < 0 or col >= len(image[0]):
        return False
    
    # Check if the current position is already visited
    if visited[row][col]:
        return False
    
    # Check if the current position is land
    if image[row][col] == 'L':
        return True
    
    return False

def dfs(image, row, col, visited):
    # Mark the current position as visited
    visited[row][col] = True
    
    # Recursively explore all adjacent positions
    if is_valid_island(image, row-1, col, visited):
        dfs(image, row-1, col, visited)
    if is_valid_island(image, row, col-1, visited):
        dfs(image, row, col-1, visited)
    if is_valid_island(image, row+1, col, visited):
        dfs(image, row+1, col, visited)
    if is_valid_island(image, row, col+1, visited):
        dfs(image, row, col+1, visited)

def num_islands(image):
    # Initialize the visited array
    visited = [[False for _ in range(len(image[0]))] for _ in range(len(image))]
    
    # Initialize the number of islands
    num_islands = 0
    
    # Iterate through the image
    for row in range(len(image)):
        for col in range(len(image[0])):
            # Check if the current position is land and has not been visited yet
            if image[row][col] == 'L' and not visited[row][col]:
                # Perform depth-first search from the current position
                dfs(image, row, col, visited)
                num_islands += 1
    
    return num_islands

def main():
    # Read the input
    r, c = map(int, input().split())
    image = [input() for _ in range(r)]
    
    # Find the number of islands
    num_islands = num_islands(image)
    
    # Print the result
    print(num_islands)

if __name__ == '__main__':
    main()

