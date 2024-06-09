
def get_max_beauty(n, k, x, a):
    # Calculate the sum of beauty values of all pictures
    total_beauty = sum(a)

    # Check if it's possible to repost x pictures and still satisfy the condition
    if x > n:
        return -1

    # Initialize the maximum sum of beauty values to 0
    max_beauty = 0

    # Loop through all possible combinations of reposted pictures
    for i in range(1 << n):
        # Calculate the number of reposted pictures
        num_reposted = bin(i).count("1")

        # Check if the number of reposted pictures is valid
        if num_reposted != x:
            continue

        # Calculate the sum of beauty values of reposted pictures
        reposted_beauty = 0
        for j in range(n):
            if i & (1 << j):
                reposted_beauty += a[j]

        # Check if the sum of beauty values is maximum possible
        if reposted_beauty > max_beauty:
            max_beauty = reposted_beauty

    # Return the maximum sum of beauty values
    return max_beauty

