
def solve(m, k):
    # Calculate the maximum number of bags that can be weighed in m weighings
    max_bags = m * k
    
    # Calculate the maximum number of weighings needed to determine the fake bag
    # among bags containing k coins
    max_weighings = k - 1
    
    # Return the minimum of the maximum number of bags and the maximum number of weighings
    return min(max_bags, max_weighings) % 998244353

