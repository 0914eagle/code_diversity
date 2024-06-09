
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
            # Increment the current area
            current_area += 1
        # Check if the current cell is 0
        elif matrix[top_row][left_col] == "0":
            # Check if the current area is greater than the max area
            if current_area > max_area:
                max_area = current_area
            # Reset the current area
            current_area = 0
        # Increment the top row
        top_row += 1
    
    # Return the max area
    return max_area

def main():
    # Test the get_largest_rectangle function
    matrix = [
      ["1","0","1","0","0"],
      ["1","0","1","1","1"],
      ["1","1","1","1","1"],
      ["1","0","0","1","0"]
    ]
    print(get_largest_rectangle(matrix))

if __name__ == '__main__':
    main()

