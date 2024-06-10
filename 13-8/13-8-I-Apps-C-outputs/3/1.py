
def get_subset_cost(n, k):
    # Calculate the cost of having each subset
    subset_costs = [1]
    for i in range(1, n):
        subset_costs.append(subset_costs[i-1] * k)
    
    # Calculate the sum of costs for all non-empty subsets
    total_cost = 0
    for cost in subset_costs:
        total_cost += cost
    
    return total_cost % (10**9 + 7)

def main():
    n, k = map(int, input().split())
    print(get_subset_cost(n, k))

if __name__ == '__main__':
    main()

