
def get_moving_cost(costs):
    # Initialize variables
    n = len(costs)
    dp = [0] * (n + 1)
    
    # Populate the dp table
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            dp[i] = min(dp[i], dp[i - j] + costs[j - 1])
    
    # Return the minimum moving cost
    return dp[n]

def main():
    # Read the input
    n, k = map(int, input().split())
    costs = []
    for i in range(n):
        costs.append(list(map(int, input().split())))
    
    # Call the get_moving_cost function
    moving_cost = get_moving_cost(costs)
    
    # Print the minimum moving cost
    print(moving_cost)

if __name__ == '__main__':
    main()

