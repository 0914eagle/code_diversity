
def get_optimal_strategy(n, p, assignment):
    # Initialize the optimal strategy as an empty string
    optimal_strategy = ""
    
    # Loop through each piece and check if it is assigned to team A or B
    for i in range(n):
        # If the piece is assigned to team A, append a 1 to the optimal strategy
        if assignment[i] == "A":
            optimal_strategy += "1"
        # If the piece is assigned to team B, append a 0 to the optimal strategy
        else:
            optimal_strategy += "0"
    
    # Return the optimal strategy
    return optimal_strategy

def get_maximum_strength(n, p, assignment, optimal_strategy):
    # Initialize the maximum strength as 0
    maximum_strength = 0
    
    # Loop through each piece and check if it is assigned to team A or B
    for i in range(n):
        # If the piece is assigned to team A and the optimal strategy is 1, add its strength to the maximum strength
        if assignment[i] == "A" and optimal_strategy[i] == "1":
            maximum_strength += p[i]
        # If the piece is assigned to team B and the optimal strategy is 0, add its strength to the maximum strength
        elif assignment[i] == "B" and optimal_strategy[i] == "0":
            maximum_strength += p[i]
    
    # Return the maximum strength
    return maximum_strength

if __name__ == '__main__':
    n = int(input())
    p = list(map(int, input().split()))
    assignment = input()
    optimal_strategy = get_optimal_strategy(n, p, assignment)
    maximum_strength = get_maximum_strength(n, p, assignment, optimal_strategy)
    print(maximum_strength)

