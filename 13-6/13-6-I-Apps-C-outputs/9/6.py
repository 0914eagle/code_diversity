
def get_rectangle_area(n_r, n_c, rows, cols):
    
    # Initialize a grid to keep track of the icons
    grid = [[0 for _ in range(n_c)] for _ in range(n_r)]

    # Mark the icons as 1 in the grid
    for r, c in zip(rows, cols):
        grid[r][c] = 1

    # Initialize the number of icons to move
    num_icons_to_move = 0

    # Iterate through the grid and check if there are any adjacent icons that can be moved
    for r in range(n_r):
        for c in range(n_c):
            if grid[r][c] == 1:
                # Check if there are any adjacent icons that can be moved
                if r > 0 and grid[r-1][c] == 1:
                    grid[r-1][c] = 0
                    num_icons_to_move += 1
                if c > 0 and grid[r][c-1] == 1:
                    grid[r][c-1] = 0
                    num_icons_to_move += 1
                if r < n_r-1 and grid[r+1][c] == 1:
                    grid[r+1][c] = 0
                    num_icons_to_move += 1
                if c < n_c-1 and grid[r][c+1] == 1:
                    grid[r][c+1] = 0
                    num_icons_to_move += 1

    return num_icons_to_move

def main():
    n_r, n_c, n, m = map(int, input().split())
    rows = [int(x) for x in input().split()]
    cols = [int(x) for x in input().split()]
    print(get_rectangle_area(n_r, n_c, rows, cols))

if __name__ == '__main__':
    main()

