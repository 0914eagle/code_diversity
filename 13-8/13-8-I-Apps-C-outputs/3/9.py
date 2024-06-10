
def get_subset_costs(n, k):
    # Calculate the number of non-empty subsets
    num_subsets = 2**n - 1
    
    # Initialize a list to store the costs of all non-empty subsets
    subset_costs = [0] * num_subsets
    
    # Iterate over each non-empty subset
    for i in range(num_subsets):
        # Calculate the cost of the current subset
        subset_costs[i] = (i+1)**k
    
    # Return the sum of the costs modulo 10^9 + 7
    return sum(subset_costs) % (10**9 + 7)

def main():
    n, k = map(int, input().split())
    print(get_subset_costs(n, k))

if __name__ == '__main__':
    main()

