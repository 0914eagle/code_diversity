
def get_max_earnings(a):
    # Initialize variables
    n = len(a)
    smashed = [False] * n
    earnings = 0

    # Iterate through the gems
    for i in range(n):
        # If the gem is not smashed and has a positive value, smash it
        if not smashed[i] and a[i] > 0:
            # Smash the gem and add its value to the earnings
            smashed[i] = True
            earnings += a[i]

            # Smash all gems that are multiples of the current gem
            for j in range(i + i, n, i):
                if not smashed[j]:
                    smashed[j] = True
                    earnings += a[j]

    # Return the maximum earnings
    return earnings

