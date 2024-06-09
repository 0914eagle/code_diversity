
def get_maximum_area_of_subsquare(sub_rectangle):
    
    # Initialize the maximum area to 0
    maximum_area = 0
    
    # Loop through each row of the sub-rectangle
    for i in range(sub_rectangle.shape[0]):
        # Loop through each column of the sub-rectangle
        for j in range(sub_rectangle.shape[1]):
            # Check if the current cell is a Nanosoft logo
            if is_nanosoft_logo(sub_rectangle[i, j]):
                # If it is, find the maximum area of the sub-square
                maximum_area = max(maximum_area, get_area_of_subsquare(sub_rectangle, i, j))
    
    # Return the maximum area
    return maximum_area

def is_nanosoft_logo(cell):
    
    # Check if the cell is a Nanosoft logo
    if cell == "R" or cell == "G" or cell == "Y" or cell == "B":
        return True
    else:
        return False

def get_area_of_subsquare(sub_rectangle, row, column):
    
    # Initialize the area to 0
    area = 0
    
    # Loop through each row of the sub-square
    for i in range(row, row + 2):
        # Loop through each column of the sub-square
        for j in range(column, column + 2):
            # Check if the current cell is a Nanosoft logo
            if is_nanosoft_logo(sub_rectangle[i, j]):
                # If it is, increment the area
                area += 1
    
    # Return the area
    return area

def main():
    # Read the input
    n, m, q = map(int, input().split())
    grid = []
    for _ in range(n):
        grid.append(list(input()))
    
    # Loop through each option
    for _ in range(q):
        # Read the option
        r1, c1, r2, c2 = map(int, input().split())
        
        # Get the sub-rectangle for the option
        sub_rectangle = grid[r1-1:r2, c1-1:c2]
        
        # Get the maximum area of a sub-square inside the sub-rectangle
        maximum_area = get_maximum_area_of_subsquare(sub_rectangle)
        
        # Print the maximum area
        print(maximum_area)

if __name__ == '__main__':
    main()

