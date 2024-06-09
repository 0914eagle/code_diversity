
def solve(a, X):
    # Calculate the maximum number of candies Binod can collect on each day
    max_candies = [0] * len(a)
    for i in range(len(a)):
        max_candies[i] = a[i] + X

    # Calculate the maximum number of candies Binod can collect after the festival ends
    max_candies_total = 0
    for i in range(len(a)):
        max_candies_total += max_candies[i]

    return max_candies_total

