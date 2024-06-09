
def get_max_beauty(n, k, x, a):
    # Calculate the maximum sum of beauty values of reposted pictures
    max_beauty = 0
    for i in range(n - k + 1):
        # Sum the beauty values of the current segment
        segment_beauty = sum(a[i:i+k])
        # Check if reposting the current segment would exceed the maximum number of reposts allowed
        if segment_beauty > max_beauty and x - 1 >= 0:
            max_beauty = segment_beauty
            x -= 1
    # If all segments have been processed and there are still reposts left, it is not possible to satisfy all conditions
    if x > 0:
        return -1
    else:
        return max_beauty

