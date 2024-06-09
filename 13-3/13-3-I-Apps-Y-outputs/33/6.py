
def get_max_beauty(n, k, x, a):
    # Calculate the maximum sum of beauty values of reposted pictures
    max_beauty = 0
    for i in range(n - k + 1):
        # Calculate the sum of beauty values of the current segment
        segment_beauty = sum(a[i:i+k])
        # Check if the current segment has at least one picture reposted by Vova
        if segment_beauty > 0:
            # Add the current segment to the total sum of beauty values
            max_beauty += segment_beauty
            # Decrement the number of pictures Vova is ready to repost
            x -= 1
            # If Vova has reposted all the pictures, return the maximum sum of beauty values
            if x == 0:
                return max_beauty
    # If there is no way to repost some pictures to satisfy all the conditions, return -1
    if x > 0:
        return -1
    else:
        return max_beauty

