
def read_input():
    r, c = map(int, input().split())
    image = [input() for _ in range(r)]
    return image

def get_islands(image):
    # Initialize a 2D array to keep track of visited cells
    visited = [[False for _ in range(c)] for _ in range(r)]
    
    # Initialize a counter for the number of islands
    num_islands = 0
    
    # Iterate through the image
    for i in range(r):
        for j in range(c):
            # If the current cell is land and has not been visited yet, explore the island and increment the counter
            if image[i][j] == 'L' and not visited[i][j]:
                explore_island(image, visited, i, j)
                num_islands += 1
    
    return num_islands

def explore_island(image, visited, i, j):
    # Mark the current cell as visited
    visited[i][j] = True
    
    # If the current cell is not at the boundary of the image, explore the surrounding cells
    if i > 0 and not visited[i-1][j] and image[i-1][j] == 'L':
        explore_island(image, visited, i-1, j)
    if i < r-1 and not visited[i+1][j] and image[i+1][j] == 'L':
        explore_island(image, visited, i+1, j)
    if j > 0 and not visited[i][j-1] and image[i][j-1] == 'L':
        explore_island(image, visited, i, j-1)
    if j < c-1 and not visited[i][j+1] and image[i][j+1] == 'L':
        explore_island(image, visited, i, j+1)

def main():
    image = read_input()
    print(get_islands(image))

if __name__ == '__main__':
    main()

