
def get_islands(image):
    # Initialize a 2D array to keep track of visited cells
    visited = [[False for _ in range(len(image[0]))] for _ in range(len(image))]
    
    # Initialize a counter for the number of islands
    num_islands = 0
    
    # Loop through each cell in the image
    for i in range(len(image)):
        for j in range(len(image[0])):
            # If the current cell is not visited and is land, explore the island and increment the counter
            if not visited[i][j] and image[i][j] == 'L':
                explore_island(image, visited, i, j)
                num_islands += 1
    
    return num_islands

def explore_island(image, visited, i, j):
    # If the current cell is out of bounds or not land, return
    if i < 0 or i >= len(image) or j < 0 or j >= len(image[0]) or image[i][j] != 'L' or visited[i][j]:
        return
    
    # Mark the current cell as visited
    visited[i][j] = True
    
    # Recursively explore the island in all four directions
    explore_island(image, visited, i-1, j)
    explore_island(image, visited, i+1, j)
    explore_island(image, visited, i, j-1)
    explore_island(image, visited, i, j+1)

def main():
    # Read the input image
    r, c = map(int, input().split())
    image = [input() for _ in range(r)]
    
    # Get the number of islands in the image
    num_islands = get_islands(image)
    
    # Print the number of islands
    print(num_islands)

if __name__ == '__main__':
    main()

