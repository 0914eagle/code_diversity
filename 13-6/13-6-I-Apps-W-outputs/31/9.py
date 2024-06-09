
def get_max_area(picture, r1, c1, r2, c2):
    # Initialize the maximum area to 0
    max_area = 0
    
    # Loop through the rows and columns of the sub-rectangle
    for i in range(r1, r2 + 1):
        for j in range(c1, c2 + 1):
            # If the current cell is red, increment the maximum area by 1
            if picture[i][j] == "R":
                max_area += 1
    
    # Return the maximum area
    return max_area

def get_sub_square(picture, r1, c1, r2, c2):
    # Initialize the sub-square with the top-left corner in (r1, c1) and the bottom-right corner in (r2, c2)
    sub_square = []
    
    # Loop through the rows and columns of the sub-rectangle
    for i in range(r1, r2 + 1):
        for j in range(c1, c2 + 1):
            # If the current cell is red, append the cell to the sub-square
            if picture[i][j] == "R":
                sub_square.append((i, j))
    
    # Return the sub-square
    return sub_square

def get_max_sub_square(picture, r1, c1, r2, c2):
    # Get the maximum area of the sub-rectangle
    max_area = get_max_area(picture, r1, c1, r2, c2)
    
    # Initialize the maximum sub-square with the top-left corner in (r1, c1) and the bottom-right corner in (r2, c2)
    max_sub_square = []
    
    # Loop through the rows and columns of the sub-rectangle
    for i in range(r1, r2 + 1):
        for j in range(c1, c2 + 1):
            # If the current cell is red and its area is equal to the maximum area, append the cell to the maximum sub-square
            if picture[i][j] == "R" and get_area(picture, i, j, r2, c2) == max_area:
                max_sub_square.append((i, j))
    
    # Return the maximum sub-square
    return max_sub_square

def get_area(picture, r1, c1, r2, c2):
    # Initialize the area to 0
    area = 0
    
    # Loop through the rows and columns of the sub-rectangle
    for i in range(r1, r2 + 1):
        for j in range(c1, c2 + 1):
            # If the current cell is red, increment the area by 1
            if picture[i][j] == "R":
                area += 1
    
    # Return the area
    return area

def main():
    # Read the input
    n, m, q = map(int, input().split())
    picture = []
    for i in range(n):
        picture.append(list(input()))
    
    # Loop through the options
    for i in range(q):
        # Read the option
        r1, c1, r2, c2 = map(int, input().split())
        
        # Get the maximum sub-square
        max_sub_square = get_max_sub_square(picture, r1, c1, r2, c2)
        
        # Print the maximum area of the sub-square
        print(len(max_sub_square))

if __name__ == '__main__':
    main()

