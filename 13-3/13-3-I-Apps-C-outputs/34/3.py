
def solve(m, k):
    # Calculate the maximum number of bags that can be determined with m weighings
    max_bags = (m * (m + 1)) // 2
    
    # Calculate the maximum number of bags that can be determined with m weighings and k coins in each bag
    max_bags = max_bags // k
    
    # Return the result modulo the large prime 998244353
    return max_bags % 998244353

