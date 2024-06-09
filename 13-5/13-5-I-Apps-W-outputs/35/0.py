
def get_solution(n, m, S_x, S_y):
    # Initialize the solution matrix
    solution = [[0] * m for _ in range(n)]
    
    # Mark the starting cell as visited
    solution[S_x - 1][S_y - 1] = 1
    
    # Initialize the queue with the starting cell
    queue = [(S_x, S_y)]
    
    # Loop until the queue is empty
    while queue:
        # Get the current cell from the queue
        x, y = queue.pop(0)
        
        # Get the neighbors of the current cell
        neighbors = get_neighbors(n, m, x, y)
        
        # Loop through the neighbors
        for neighbor in neighbors:
            # If the neighbor is not visited, mark it as visited and add it to the queue
            if solution[neighbor[0] - 1][neighbor[1] - 1] == 0:
                solution[neighbor[0] - 1][neighbor[1] - 1] = 1
                queue.append(neighbor)
    
    # Return the solution matrix
    return solution

def get_neighbors(n, m, x, y):
    # Get the neighbors of the current cell
    neighbors = [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]
    
    # Filter the neighbors that are out of bounds
    neighbors = [neighbor for neighbor in neighbors if 1 <= neighbor[0] <= n and 1 <= neighbor[1] <= m]
    
    # Return the filtered neighbors
    return neighbors

def print_solution(solution):
    # Loop through the solution matrix
    for i in range(len(solution)):
        for j in range(len(solution[0])):
            # If the cell is visited, print its coordinates
            if solution[i][j] == 1:
                print(i + 1, j + 1)

if __name__ == '__main__':
    n, m, S_x, S_y = map(int, input().split())
    solution = get_solution(n, m, S_x, S_y)
    print_solution(solution)

