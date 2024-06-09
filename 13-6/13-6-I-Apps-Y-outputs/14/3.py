
def get_max_beauty(n, k, x, a):
    # Calculate the maximum sum of values of reposted pictures
    max_beauty = 0
    for i in range(n - k + 1):
        # Calculate the sum of beauty values of reposted pictures
        beauty = sum(a[i:i+x])
        # Check if the sum of beauty values is maximum possible
        if beauty > max_beauty:
            max_beauty = beauty
    # Return the maximum sum of values of reposted pictures
    return max_beauty

