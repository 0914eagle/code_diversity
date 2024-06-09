
def solve(a, x):
    # Calculate the maximum number of candies Binod can collect on each day
    max_candies = [0] * len(a)
    for i in range(len(a)):
        max_candies[i] = a[i] + x

    # Calculate the maximum number of candies Binod can collect over all days
    max_total_candies = 0
    for i in range(len(a)):
        max_total_candies += max_candies[i]

    return max_total_candies

