
def get_max_area(grid, r1, c1, r2, c2):
    # Initialize the maximum area to 0
    max_area = 0
    
    # Loop through the rows and columns of the sub-rectangle
    for i in range(r1, r2 + 1):
        for j in range(c1, c2 + 1):
            # If the current cell is red, green, yellow, or blue
            if grid[i][j] in ["R", "G", "Y", "B"]:
                # Find the area of the sub-square with the current cell as its center
                area = get_sub_square_area(grid, i, j)
                # Update the maximum area if the current area is greater than the previous maximum area
                if area > max_area:
                    max_area = area
    
    # Return the maximum area
    return max_area

def get_sub_square_area(grid, r, c):
    # Initialize the area to 0
    area = 0
    
    # Loop through the four directions (up, down, left, and right)
    for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        # Find the length of the sub-square in the current direction
        length = get_sub_square_length(grid, r, c, direction)
        # Update the area if the length is greater than 0
        if length > 0:
            area += length ** 2
    
    # Return the area
    return area

def get_sub_square_length(grid, r, c, direction):
    # Initialize the length to 0
    length = 0
    
    # Loop through the cells in the current direction
    while True:
        # Find the next cell in the current direction
        next_r = r + direction[0]
        next_c = c + direction[1]
        
        # If the next cell is outside the grid or has a different color, break the loop
        if next_r < 0 or next_r >= len(grid) or next_c < 0 or next_c >= len(grid[0]) or grid[next_r][next_c] != grid[r][c]:
            break
        
        # Update the length and move to the next cell
        length += 1
        r = next_r
        c = next_c
    
    # Return the length
    return length

def main():
    # Read the input
    n, m, q = map(int, input().split())
    grid = [input() for _ in range(n)]
    for _ in range(q):
        r1, c1, r2, c2 = map(int, input().split())
        
        # Call the function to find the maximum area of a sub-square inside the given sub-rectangle
        max_area = get_max_area(grid, r1, c1, r2, c2)
        
        # Print the maximum area
        print(max_area)

if __name__ == '__main__':
    main()

