
def get_maximum_candies(n, k):
    # Calculate the minimum number of candies that each kid should receive
    min_candies = n // k
    # Calculate the maximum number of candies that each kid can receive
    max_candies = min_candies + 1
    # Calculate the number of kids that can receive the minimum number of candies
    min_kids = n // min_candies
    # Calculate the number of kids that can receive the maximum number of candies
    max_kids = n // max_candies
    # If the number of kids that can receive the minimum number of candies is less than or equal to the floor of k/2, return the minimum number of candies
    if min_kids <= k//2:
        return min_candies
    # If the number of kids that can receive the maximum number of candies is less than or equal to the floor of k/2, return the maximum number of candies
    elif max_kids <= k//2:
        return max_candies
    # Otherwise, return the minimum number of candies plus 1
    else:
        return min_candies + 1

