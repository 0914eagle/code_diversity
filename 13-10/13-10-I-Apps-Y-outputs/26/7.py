
def get_coloring(a, b):
    # Initialize the board as a 2D array of zeros
    board = [[0] * (a + b) for _ in range(a + b)]
    
    # Fill the board with the correct coloring
    for i in range(a):
        for j in range(b):
            if i + j < a - 1 and i + j < b - 1:
                board[i][j] = 1
            else:
                board[i][j] = 2
    
    # Find the length of the perimeter of the rectangle
    perimeter = 0
    for i in range(a):
        for j in range(b):
            if board[i][j] == 1:
                perimeter += 1
    
    return perimeter

def main():
    a, b = map(int, input().split())
    print(get_coloring(a, b))

if __name__ == '__main__':
    main()

