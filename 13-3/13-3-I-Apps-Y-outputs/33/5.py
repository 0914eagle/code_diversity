
def get_max_beauty(n, k, x, a):
    # Calculate the maximum sum of beauty values of reposted pictures
    max_beauty = 0
    for i in range(n - k + 1):
        # Calculate the sum of beauty values of the current segment
        segment_beauty = sum(a[i:i+k])
        # Check if the current segment has at least one picture reposted by Vova
        if segment_beauty >= x:
            max_beauty = max(max_beauty, segment_beauty)
    # Return -1 if there is no way to repost some pictures to satisfy all conditions
    if max_beauty == 0:
        return -1
    # Return the maximum sum of beauty values of reposted pictures
    return max_beauty

