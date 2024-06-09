
def get_largest_rectangle(matrix):
    # Initialize variables
    max_area = 0
    current_area = 0
    top_row = 0
    bottom_row = len(matrix) - 1
    left_col = 0
    right_col = len(matrix[0]) - 1
    
    # Loop through the matrix
    while top_row <= bottom_row and left_col <= right_col:
        # Check if the current cell is 1
        if matrix[top_row][left_col] == "1":
            # Update the current area
            current_area += 1
        else:
            # If the current cell is 0, update the maximum area
            max_area = max(max_area, current_area)
            current_area = 0
        
        # Update the top row and bottom row
        top_row += 1
        bottom_row -= 1
        
        # Update the left column and right column
        left_col += 1
        right_col -= 1
    
    # Return the maximum area
    return max_area

def main():
    # Test the function with an example matrix
    matrix = [
      ["1","0","1","0","0"],
      ["1","0","1","1","1"],
      ["1","1","1","1","1"],
      ["1","0","0","1","0"]
    ]
    print(get_largest_rectangle(matrix))

if __name__ == '__main__':
    main()

