
def get_min_perimeter(a, b):
    # Initialize variables
    min_perimeter = float('inf')
    red_tiles = []
    blue_tiles = []
    
    # Iterate through all possible combinations of red and blue tiles
    for i in range(a):
        for j in range(b):
            # Check if the current combination forms a rectangle
            if i + j == a + b - 2:
                # Check if the current combination has a smaller perimeter than the current minimum
                perimeter = get_perimeter(i, j, a, b)
                if perimeter < min_perimeter:
                    min_perimeter = perimeter
                    red_tiles = [i]
                    blue_tiles = [j]
    
    # Return the minimum perimeter and the corresponding colored tiles
    return min_perimeter, red_tiles, blue_tiles

def get_perimeter(i, j, a, b):
    # Calculate the perimeter of the rectangle formed by the current combination of red and blue tiles
    perimeter = 0
    perimeter += i + j
    perimeter += a - i
    perimeter += b - j
    return perimeter

if __name__ == '__main__':
    a, b = map(int, input().split())
    min_perimeter, red_tiles, blue_tiles = get_min_perimeter(a, b)
    print(min_perimeter)

