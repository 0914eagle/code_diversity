
def get_subsets(N, k):
    # Calculate the number of non-empty subsets
    num_subsets = 2**N - 1
    
    # Initialize a list to store the costs
    costs = [0] * num_subsets
    
    # Iterate over each non-empty subset
    for i in range(num_subsets):
        # Calculate the cost of the current subset
        cost = 0
        for j in range(N):
            if i & (1 << j):
                cost += j**k
        costs[i] = cost
    
    # Return the sum of costs modulo 10^9 + 7
    return sum(costs) % (10**9 + 7)

def main():
    N, k = map(int, input().split())
    print(get_subsets(N, k))

if __name__ == '__main__':
    main()

