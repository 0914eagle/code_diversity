
def get_max_logo_area(picture, sub_rectangle):
    
    # Initialize the maximum area to 0
    max_area = 0
    
    # Get the rows and columns of the sub-rectangle
    rows = sub_rectangle[0]
    cols = sub_rectangle[1]
    
    # Loop through the rows and columns of the sub-rectangle
    for i in range(rows, rows + 2):
        for j in range(cols, cols + 2):
            # Check if the current cell is part of a Nanosoft logo
            if is_nanosoft_logo(picture, i, j):
                # Calculate the area of the current Nanosoft logo
                area = (j - cols + 1) * (i - rows + 1)
                # Update the maximum area if necessary
                max_area = max(max_area, area)
    
    # Return the maximum area
    return max_area

def is_nanosoft_logo(picture, row, col):
    
    # Get the color of the current cell
    color = picture[row][col]
    
    # Check if the current cell is part of a Nanosoft logo
    if color == "R" and (row, col) in [(1, 1), (1, 2), (2, 1), (2, 2)]:
        return True
    elif color == "G" and (row, col) in [(1, 3), (1, 4), (2, 3), (2, 4)]:
        return True
    elif color == "Y" and (row, col) in [(3, 1), (3, 2), (4, 1), (4, 2)]:
        return True
    elif color == "B" and (row, col) in [(3, 3), (3, 4), (4, 3), (4, 4)]:
        return True
    else:
        return False

def main():
    # Read the input
    n, m, q = map(int, input().split())
    picture = [input() for _ in range(n)]
    for _ in range(q):
        sub_rectangle = list(map(int, input().split()))
        # Call the function to get the maximum area of a Nanosoft logo inside the sub-rectangle
        max_area = get_max_logo_area(picture, sub_rectangle)
        # Print the result
        print(max_area)

if __name__ == "__main__":
    main()

