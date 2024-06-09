
def solve(a, X):
    # Calculate the maximum number of candies Binod can collect on each day
    max_candies = [0] * len(a)
    for i in range(len(a)):
        max_candies[i] = a[i] + X

    # Calculate the maximum number of candies Binod can collect after the festival ends
    max_total_candies = 0
    for i in range(len(a)):
        max_total_candies += max_candies[i]

    return max_total_candies

