
def get_maximum_tastiness(n, k, a, b, tastiness, complementary_pairs):
    # Initialize the dp table with 0 for all indices
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    
    # Loop through all possible number of scoops
    for i in range(1, n + 1):
        # Loop through all possible flavors
        for j in range(1, k + 1):
            # Get the tastiness of the current scoop
            tastiness_j = tastiness[j - 1]
            
            # Loop through all possible flavors that can be on top of the current scoop
            for l in range(1, k + 1):
                # If the flavors are complementary, add the tastiness of the complementary pair
                if [j, l] in complementary_pairs:
                    tastiness_j += tastiness[l - 1]
                
                # Get the maximum tastiness by trying all possible number of scoops of flavor l
                dp[i][j] = max(dp[i][j], dp[i - 1][l] + tastiness_j)
    
    # Return the maximum tastiness
    return dp[n][1]

def get_maximum_tastiness_ratio(n, k, a, b, tastiness, complementary_pairs):
    # Get the maximum tastiness
    maximum_tastiness = get_maximum_tastiness(n, k, a, b, tastiness, complementary_pairs)
    
    # Calculate the cost of the ice cream
    cost = a * n + b
    
    # Return the maximum tastiness ratio
    return maximum_tastiness / cost

if __name__ == '__main__':
    n, k, a, b = map(int, input().split())
    tastiness = list(map(int, input().split()))
    complementary_pairs = []
    for i in range(k):
        complementary_pairs.extend(list(map(int, input().split())))
    print(get_maximum_tastiness_ratio(n, k, a, b, tastiness, complementary_pairs))

