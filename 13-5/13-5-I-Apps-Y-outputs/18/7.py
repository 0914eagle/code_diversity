
def get_islands(image):
    # Initialize a dictionary to store the number of islands for each cell
    num_islands = {}
    
    # Loop through each cell in the image
    for row in range(len(image)):
        for col in range(len(image[0])):
            # If the cell is land and not already part of an island, create a new island
            if image[row][col] == "L" and (row, col) not in num_islands:
                num_islands[(row, col)] = 1
                dfs(image, row, col, num_islands)
    
    # Return the total number of islands
    return sum(num_islands.values())

def dfs(image, row, col, num_islands):
    # Base case: if the cell is water or already part of an island, return
    if image[row][col] == "W" or (row, col) in num_islands:
        return
    
    # Mark the current cell as part of an island
    num_islands[(row, col)] = 1
    
    # Recursively explore the four neighboring cells
    if row > 0:
        dfs(image, row-1, col, num_islands)
    if row < len(image)-1:
        dfs(image, row+1, col, num_islands)
    if col > 0:
        dfs(image, row, col-1, num_islands)
    if col < len(image[0])-1:
        dfs(image, row, col+1, num_islands)

def main():
    # Read the input image
    r, c = map(int, input().split())
    image = [input() for _ in range(r)]
    
    # Call the get_islands function and print the result
    print(get_islands(image))

if __name__ == '__main__':
    main()

