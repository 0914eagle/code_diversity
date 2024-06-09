
def get_max_area(picture, r1, c1, r2, c2):
    # Initialize the maximum area to 0
    max_area = 0
    
    # Loop through the rows and columns of the sub-rectangle
    for i in range(r1, r2+1):
        for j in range(c1, c2+1):
            # If the current cell is part of a Nanosoft logo, update the maximum area
            if is_nanosoft_logo(picture, i, j):
                max_area = max(max_area, get_square_area(picture, i, j))
    
    # Return the maximum area
    return max_area

def is_nanosoft_logo(picture, r, c):
    # If the current cell is not part of a Nanosoft logo, return False
    if picture[r][c] != 'R':
        return False
    
    # If the current cell is the top left square, return True
    if r == 1 and c == 1:
        return True
    
    # If the current cell is not the top left square, check if it is part of a Nanosoft logo
    return is_nanosoft_logo(picture, r-1, c-1) and is_nanosoft_logo(picture, r, c-1) and is_nanosoft_logo(picture, r-1, c)

def get_square_area(picture, r, c):
    # Initialize the area to 0
    area = 0
    
    # Loop through the rows and columns of the sub-square
    for i in range(r, r+2):
        for j in range(c, c+2):
            # If the current cell is part of a Nanosoft logo, update the area
            if is_nanosoft_logo(picture, i, j):
                area += 1
    
    # Return the area
    return area

def main():
    # Read the input
    n, m, q = map(int, input().split())
    picture = [input() for _ in range(n)]
    options = [list(map(int, input().split())) for _ in range(q)]
    
    # Loop through the options
    for option in options:
        # Get the maximum area of the sub-square inside the given sub-rectangle
        max_area = get_max_area(picture, option[0], option[1], option[2], option[3])
        
        # Print the maximum area
        print(max_area)

if __name__ == '__main__':
    main()

