
def get_cost(cost_matrix, current_value, target_value):
    # If the current value is the target value, return 0
    if current_value == target_value:
        return 0
    
    # If the current value is -1, return -1
    if current_value == -1:
        return -1
    
    # Initialize the minimum cost to infinity
    min_cost = float('inf')
    
    # Iterate over the possible values that can be transformed into the target value
    for i in range(10):
        # If the current value is equal to the target value, return 0
        if current_value == i:
            continue
        
        # Get the cost of transforming the current value into the target value
        cost = cost_matrix[current_value][i]
        
        # If the cost is -1, it means that the transformation is not possible, so skip this value
        if cost == -1:
            continue
        
        # Get the cost of transforming the current value into the target value and then into 1
        total_cost = cost + get_cost(cost_matrix, i, target_value)
        
        # If the total cost is less than the minimum cost, update the minimum cost
        if total_cost < min_cost:
            min_cost = total_cost
    
    return min_cost

def solve(cost_matrix, wall):
    # Initialize the minimum total cost to infinity
    min_total_cost = float('inf')
    
    # Iterate over the rows of the wall
    for i in range(len(wall)):
        # Iterate over the columns of the wall
        for j in range(len(wall[0])):
            # If the current value is not -1, skip this value
            if wall[i][j] == -1:
                continue
            
            # Get the cost of transforming the current value into 1
            cost = get_cost(cost_matrix, wall[i][j], 1)
            
            # If the cost is -1, it means that the transformation is not possible, so skip this value
            if cost == -1:
                continue
            
            # Get the total cost of transforming the current value into 1 and then into 1
            total_cost = cost + get_cost(cost_matrix, 1, 1)
            
            # If the total cost is less than the minimum total cost, update the minimum total cost
            if total_cost < min_total_cost:
                min_total_cost = total_cost
    
    return min_total_cost

def main():
    # Read the input from stdin
    H, W = map(int, input().split())
    cost_matrix = []
    for _ in range(10):
        cost_matrix.append(list(map(int, input().split())))
    wall = []
    for _ in range(H):
        wall.append(list(map(int, input().split())))
    
    # Solve the problem
    result = solve(cost_matrix, wall)
    
    # Output the result
    print(result)

if __name__ == '__main__':
    main()

