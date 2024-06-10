
def can_make_symmetric(H, W, grid):
    # Initialize a matrix to store the results of the swaps
    swapped = [[False for _ in range(W)] for _ in range(H)]
    
    # Loop through each row and column and check if the letters are the same
    for i in range(H):
        for j in range(W):
            # Check if the letter in the current square is the same as the letter in the corresponding square in the opposite row and column
            if grid[i][j] != grid[H-i-1][W-j-1]:
                # If the letters are not the same, check if the swaps have already been made
                if not (swapped[i][j] or swapped[H-i-1][W-j-1]):
                    # If the swaps have not been made, make them and mark the squares as swapped
                    swapped[i][j] = True
                    swapped[H-i-1][W-j-1] = True
                    grid[i][j], grid[H-i-1][W-j-1] = grid[H-i-1][W-j-1], grid[i][j]
    
    # Check if all the letters are the same in the grid
    for i in range(H):
        for j in range(W):
            if grid[i][j] != grid[H-i-1][W-j-1]:
                return "NO"
    
    return "YES"

def main():
    H, W = map(int, input().split())
    grid = [input() for _ in range(H)]
    print(can_make_symmetric(H, W, grid))

if __name__ == '__main__':
    main()

