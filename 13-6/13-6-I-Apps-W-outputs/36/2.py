
def get_maximum_strength(n, p, assignment):
    # Initialize variables
    strength_a = 0
    strength_b = 0
    
    # Iterate through the game pieces
    for i in range(n):
        # If the piece is assigned to team A
        if assignment[i] == 'A':
            strength_a += p[i]
        # If the piece is assigned to team B
        else:
            strength_b += p[i]
    
    # Return the maximum strength
    return max(strength_a, strength_b)

def get_optimal_strategy(n, p, assignment):
    # Initialize variables
    optimal_strategy = ''
    current_strength = 0
    
    # Iterate through the game pieces
    for i in range(n):
        # If the piece is assigned to team A
        if assignment[i] == 'A':
            current_strength += p[i]
        # If the piece is assigned to team B
        else:
            current_strength -= p[i]
        
        # If the current strength is greater than the optimal strength
        if current_strength > 0:
            optimal_strategy += 'A'
        # If the current strength is less than the optimal strength
        else:
            optimal_strategy += 'B'
    
    # Return the optimal strategy
    return optimal_strategy

def main():
    # Read the input
    n = int(input())
    p = list(map(int, input().split()))
    assignment = input()
    
    # Get the maximum strength
    maximum_strength = get_maximum_strength(n, p, assignment)
    
    # Get the optimal strategy
    optimal_strategy = get_optimal_strategy(n, p, assignment)
    
    # Print the output
    print(maximum_strength)
    print(optimal_strategy)

if __name__ == '__main__':
    main()

