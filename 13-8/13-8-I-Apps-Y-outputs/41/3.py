
def paint_squares(height, width, squares):
    # Initialize a 2D array to store the color of each square
    canvas = [[0] * width for _ in range(height)]

    # Loop through each square and check if it is '#'
    for i in range(height):
        for j in range(width):
            if squares[i][j] == '#':
                # If the square is '#', paint it black
                canvas[i][j] = 1

    # Check if all the squares with '#' are painted black
    for i in range(height):
        for j in range(width):
            if squares[i][j] == '#' and canvas[i][j] == 0:
                return False

    return True

def main():
    height, width = map(int, input().split())
    squares = []
    for _ in range(height):
        squares.append(input())
    result = paint_squares(height, width, squares)
    print("Yes" if result else "No")

if __name__ == '__main__':
    main()

