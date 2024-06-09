
def get_maximum_strength(n, p, assignment):
    # Initialize the maximum strength and the prefix or suffix to flip
    max_strength = 0
    prefix_or_suffix = ""
    
    # Iterate over all possible prefixes or suffixes of length 1 to n-1
    for i in range(1, n):
        # Get the prefix or suffix of length i
        prefix_or_suffix = assignment[:i]
        
        # Get the strength of the pieces in the prefix or suffix
        prefix_or_suffix_strength = sum(p[j] for j in range(n) if assignment[j] == prefix_or_suffix[j])
        
        # If the strength of the prefix or suffix is greater than the current maximum strength, update the maximum strength and the prefix or suffix to flip
        if prefix_or_suffix_strength > max_strength:
            max_strength = prefix_or_suffix_strength
            prefix_or_suffix = prefix_or_suffix
    
    # Return the maximum strength and the prefix or suffix to flip
    return max_strength, prefix_or_suffix

def get_optimal_strategy(n, p, assignment):
    # Get the maximum strength and the prefix or suffix to flip
    max_strength, prefix_or_suffix = get_maximum_strength(n, p, assignment)
    
    # Initialize the optimal strategy as doing nothing
    optimal_strategy = "N"
    
    # If the maximum strength is not equal to the current strength of Alice's team, update the optimal strategy to flip the prefix or suffix
    if max_strength != sum(p[j] for j in range(n) if assignment[j] == "A"):
        optimal_strategy = "F"
    
    # Return the optimal strategy
    return optimal_strategy

def main():
    # Read the input
    n = int(input())
    p = list(map(int, input().split()))
    assignment = input()
    
    # Get the optimal strategy
    optimal_strategy = get_optimal_strategy(n, p, assignment)
    
    # Print the optimal strategy
    print(optimal_strategy)

if __name__ == '__main__':
    main()

