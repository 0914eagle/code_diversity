
def solve(n, k):
    # Calculate the minimum number of candies that each kid can have
    min_candies = n // k
    # Calculate the maximum number of candies that each kid can have
    max_candies = n // k + (n % k > 0)
    # Calculate the number of kids that can have max_candies
    num_max_kids = n - k * min_candies
    # If the number of kids that can have max_candies is less than or equal to floor(k/2), return max_candies
    if num_max_kids <= k//2:
        return max_candies
    else:
        # Otherwise, return min_candies
        return min_candies

