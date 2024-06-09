
def get_optimal_strength(n, p, assignment):
    # Initialize the maximum strength and the optimal assignment
    max_strength = 0
    optimal_assignment = ""
    
    # Iterate over all possible prefixes and suffixes
    for i in range(n):
        for j in range(i, n):
            # Calculate the strength of the prefix or suffix
            strength = sum(p[i:j+1])
            
            # If the strength is greater than the maximum strength, update the maximum strength and the optimal assignment
            if strength > max_strength:
                max_strength = strength
                optimal_assignment = assignment[:i] + "".join(reversed(assignment[i:j+1])) + assignment[j+1:]
    
    # Return the maximum strength and the optimal assignment
    return max_strength, optimal_assignment

def main():
    # Read the input
    n = int(input())
    p = list(map(int, input().split()))
    assignment = input()
    
    # Call the get_optimal_strength function
    max_strength, optimal_assignment = get_optimal_strength(n, p, assignment)
    
    # Print the output
    print(max_strength)
    print(optimal_assignment)

if __name__ == '__main__':
    main()

