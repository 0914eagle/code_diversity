
def give_candies(n, k, a):
    # Initialize variables
    days = 0
    given_candies = 0

    # Loop through the days
    for i in range(n):
        # Check if Arya has enough candies to give Bran
        if given_candies + a[i] <= k:
            # Give all the candies Arya has
            given_candies += a[i]
        else:
            # Give Bran the maximum number of candies she can give (8)
            given_candies += 8

        # Check if Arya has given Bran all the candies he needs
        if given_candies == k:
            # Return the number of days it took to give Bran all the candies
            return days

        # Increment the number of days
        days += 1

    # If Arya couldn't give Bran all the candies, return -1
    return -1

