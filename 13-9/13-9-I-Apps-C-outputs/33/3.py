
def get_ice_cream(n, k, a, b, t, u):
    # Initialize the dp table
    dp = [[0] * (k+1) for _ in range(n+1)]
    
    # Loop through each state
    for i in range(1, n+1):
        for j in range(1, k+1):
            # Get the current tastiness
            current_tastiness = dp[i-1][j] + t[j-1]
            
            # Loop through each flavor
            for l in range(1, k+1):
                # Get the additional tastiness
                additional_tastiness = u[j-1][l-1]
                
                # Check if the current flavor is the same as the previous one
                if j == l:
                    # If the same, add the additional tastiness
                    current_tastiness += additional_tastiness
                else:
                    # If not, check if the current flavor is better than the previous one
                    if current_tastiness + additional_tastiness > dp[i-1][l]:
                        # If better, update the dp table
                        dp[i][l] = current_tastiness + additional_tastiness
    
    # Return the maximum tastiness
    return max(dp[n][j] for j in range(1, k+1))

def main():
    # Read the input
    n, k, a, b = map(int, input().split())
    t = list(map(int, input().split()))
    u = []
    for _ in range(k):
        u.append(list(map(int, input().split())))
    
    # Get the maximum tastiness
    result = get_ice_cream(n, k, a, b, t, u)
    
    # Print the result
    print(result)

if __name__ == '__main__':
    main()

