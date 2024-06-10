
import math

def get_subsets(n, k):
    # Calculate the number of non-empty subsets
    num_subsets = math.pow(2, n) - 1
    
    # Initialize a list to store the costs of all subsets
    costs = [0] * num_subsets
    
    # Iterate over all subsets
    for i in range(num_subsets):
        # Calculate the cost of the current subset
        cost = 0
        for j in range(n):
            if i & (1 << j):
                cost += math.pow(j + 1, k)
        
        # Add the cost to the list
        costs[i] = cost
    
    return costs

def get_sum_of_costs(costs):
    # Initialize the sum to 0
    sum = 0
    
    # Iterate over all costs and add them to the sum
    for cost in costs:
        sum += cost
    
    # Return the sum modulo 10^9 + 7
    return sum % (10**9 + 7)

def main():
    # Read the input
    n, k = map(int, input().split())
    
    # Calculate the costs of all non-empty subsets
    costs = get_subsets(n, k)
    
    # Calculate the sum of costs
    sum = get_sum_of_costs(costs)
    
    # Print the sum
    print(sum)

if __name__ == '__main__':
    main()

