
def solve(m, k):
    # Calculate the maximum number of bags that can be determined with m weighings
    max_bags = (m * (m + 1)) // 2
    
    # Return the result modulo the large prime 998244353
    return max_bags % 998244353

