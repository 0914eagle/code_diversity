
def is_objective_achievable(s):
    # Initialize the grid with the given input
    grid = [[s[i][j] for j in range(len(s[0]))] for i in range(len(s))]
    
    # Define a function to check if a square is valid (i.e., inside the grid and not painted black)
    def is_valid_square(i, j):
        return 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] != '#'
    
    # Define a function to paint a square black
    def paint_square(i, j):
        grid[i][j] = '#'
    
    # Define a function to check if the objective is achieved
    def is_objective_achieved():
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '#' and s[i][j] != '#':
                    return False
        return True
    
    # Start painting the squares
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '#' and s[i][j] == '#':
                # Paint the current square black
                paint_square(i, j)
                # Check if the objective is achieved
                if is_objective_achieved():
                    return True
                # If not, try painting the adjacent squares black
                for k in range(i-1, i+2):
                    for l in range(j-1, j+2):
                        if is_valid_square(k, l) and grid[k][l] != '#':
                            paint_square(k, l)
    
    # If we reach this point, the objective is not achievable
    return False

def main():
    s = []
    for _ in range(int(input())):
        s.append(input())
    print("Yes") if is_objective_achievable(s) else print("No")

if __name__ == '__main__':
    main()

