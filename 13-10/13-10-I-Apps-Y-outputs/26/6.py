
def get_min_perimeter(a, b):
    # Initialize variables
    min_perimeter = float('inf')
    red_tiles = []
    blue_tiles = []
    
    # Iterate through all possible combinations of red and blue tiles
    for i in range(a):
        for j in range(b):
            # Check if the current combination forms a correct coloring
            if is_correct_coloring(i, j, a, b):
                # Calculate the perimeter of the current coloring
                perimeter = get_perimeter(i, j, a, b)
                # Update the minimum perimeter if necessary
                if perimeter < min_perimeter:
                    min_perimeter = perimeter
                    red_tiles = [i]
                    blue_tiles = [j]
    
    # Return the minimum perimeter and the corresponding coloring
    return min_perimeter, (red_tiles, blue_tiles)

def is_correct_coloring(i, j, a, b):
    # Check if the current combination forms a correct coloring
    if i + j != a + b:
        return False
    
    # Initialize variables
    red_tiles = []
    blue_tiles = []
    
    # Iterate through the rows of the board
    for k in range(i):
        # Check if the current row forms a rectangle
        if is_rectangle(red_tiles, blue_tiles):
            return False
        
        # Add the current row to the list of red tiles
        red_tiles.append(k)
        
        # Iterate through the columns of the board
        for l in range(j):
            # Check if the current column forms a rectangle
            if is_rectangle(red_tiles, blue_tiles):
                return False
            
            # Add the current column to the list of blue tiles
            blue_tiles.append(l)
    
    # Check if the current combination forms a correct coloring
    return True

def is_rectangle(red_tiles, blue_tiles):
    # Initialize variables
    n = len(red_tiles)
    m = len(blue_tiles)
    rectangle = False
    
    # Iterate through the rows of the board
    for i in range(n):
        # Check if the current row forms a rectangle
        if red_tiles[i] + 1 == red_tiles[(i + 1) % n]:
            rectangle = True
            break
    
    # Iterate through the columns of the board
    for j in range(m):
        # Check if the current column forms a rectangle
        if blue_tiles[j] + 1 == blue_tiles[(j + 1) % m]:
            rectangle = True
            break
    
    # Return the result
    return rectangle

def get_perimeter(i, j, a, b):
    # Initialize variables
    red_tiles = []
    blue_tiles = []
    
    # Iterate through the rows of the board
    for k in range(i):
        # Add the current row to the list of red tiles
        red_tiles.append(k)
        
        # Iterate through the columns of the board
        for l in range(j):
            # Add the current column to the list of blue tiles
            blue_tiles.append(l)
    
    # Calculate the perimeter of the current coloring
    perimeter = 0
    for k in range(n):
        # Calculate the perimeter of the current row
        perimeter += red_tiles[k] + red_tiles[(k + 1) % n]
    
    for l in range(m):
        # Calculate the perimeter of the current column
        perimeter += blue_tiles[l] + blue_tiles[(l + 1) % m]
    
    # Return the perimeter
    return perimeter

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(get_min_perimeter(a, b))

