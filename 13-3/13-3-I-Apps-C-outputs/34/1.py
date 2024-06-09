
def solve(m, k):
    # Calculate the maximum number of bags that can be determined with m weighings
    max_bags = (m * (m + 1)) // 2
    
    # Calculate the maximum number of coins that can be weighed in each weighing
    max_coins = m * k
    
    # Calculate the maximum number of coins that can be weighed in total
    max_total_coins = max_bags * k
    
    # Calculate the maximum number of weighings needed to determine the fake bag
    max_weighings = max_total_coins // max_coins
    
    return max_weighings % 998244353

