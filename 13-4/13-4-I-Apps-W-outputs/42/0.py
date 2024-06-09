
def get_cost(cost_matrix, digit):
    # Find the cost of turning the current digit into 1
    cost = cost_matrix[digit][1]
    
    # If the current digit is not 1, find the cost of turning it into 1
    if digit != 1:
        cost += get_cost(cost_matrix, 1)
    
    return cost

def solve(cost_matrix, wall):
    # Initialize the minimum total cost to infinity
    min_cost = float('inf')
    
    # Loop through each row of the wall
    for i in range(len(wall)):
        # Loop through each column of the wall
        for j in range(len(wall[0])):
            # If the current cell contains a digit
            if wall[i][j] != -1:
                # Get the cost of turning the current digit into 1
                cost = get_cost(cost_matrix, wall[i][j])
                
                # If the current cost is less than the minimum total cost, update the minimum total cost
                if cost < min_cost:
                    min_cost = cost
    
    return min_cost

def main():
    # Read the input from stdin
    H, W = map(int, input().split())
    cost_matrix = [list(map(int, input().split())) for _ in range(10)]
    wall = [list(map(int, input().split())) for _ in range(H)]
    
    # Solve the problem
    result = solve(cost_matrix, wall)
    
    # Output the result
    print(result)

if __name__ == '__main__':
    main()

