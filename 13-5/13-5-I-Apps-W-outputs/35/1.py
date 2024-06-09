
def get_solution(n, m, S_x, S_y):
    # Initialize the solution matrix
    solution = [[0] * m for _ in range(n)]
    
    # Mark the starting cell as visited
    solution[S_x - 1][S_y - 1] = 1
    
    # Iterate through the rows
    for i in range(n):
        # Iterate through the columns
        for j in range(m):
            # If the current cell is not visited, mark it as visited and add it to the solution
            if solution[i][j] == 0:
                solution[i][j] = 1
                yield i + 1, j + 1
    
    # Return the solution
    return solution

def main():
    # Read the input
    n, m, S_x, S_y = map(int, input().split())
    
    # Get the solution
    solution = get_solution(n, m, S_x, S_y)
    
    # Print the solution
    for i, j in solution:
        print(i, j)

if __name__ == '__main__':
    main()

