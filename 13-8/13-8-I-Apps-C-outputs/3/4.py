
def get_subset_cost(N, k):
    # Calculate the total number of subsets
    total_subsets = 2**N
    
    # Initialize a list to store the costs of each subset
    subset_costs = [0] * total_subsets
    
    # Iterate over each subset
    for i in range(total_subsets):
        # Calculate the cost of the current subset
        subset_cost = 0
        for j in range(N):
            if i & (1 << j):
                subset_cost += j**k
        
        # Add the cost to the list of costs
        subset_costs[i] = subset_cost
    
    # Return the sum of the costs
    return sum(subset_costs) % (10**9 + 7)

def main():
    # Read the input
    N, k = map(int, input().split())
    
    # Calculate the sum of costs
    total_cost = get_subset_cost(N, k)
    
    # Print the output
    print(total_cost)

if __name__ == '__main__':
    main()

