
def get_max_beauty(n, k, x, a):
    # Calculate the maximum sum of beauty values of reposted pictures
    max_beauty = 0
    for i in range(n - k + 1):
        # Calculate the sum of beauty values of the current segment
        segment_beauty = sum(a[i:i+k])
        # Check if the current segment has at least one picture reposted by Vova
        if segment_beauty > 0:
            # Update the maximum sum of beauty values
            max_beauty = max(max_beauty, segment_beauty)
    # Check if the number of reposted pictures is less than or equal to x
    if max_beauty * k <= x:
        return max_beauty
    else:
        return -1

