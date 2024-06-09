
def get_max_bags(m, k):
    # Calculate the maximum number of bags that can be determined with m weighings
    max_bags = 1
    while m > 0:
        max_bags *= k
        m -= 1
    return max_bags % 998244353

