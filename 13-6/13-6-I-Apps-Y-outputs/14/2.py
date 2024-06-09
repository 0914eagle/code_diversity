
def get_max_beauty(n, k, x, a):
    # Calculate the maximum sum of beauty values of reposted pictures
    max_sum = 0
    for i in range(n - k + 1):
        # Calculate the sum of beauty values of the current segment
        curr_sum = sum(a[i:i+k])
        # Check if the current segment has at least one picture reposted
        if curr_sum > 0:
            # Add the current segment to the maximum sum
            max_sum += curr_sum
            # Decrement the number of pictures Vova is ready to repost
            x -= 1
            # If all pictures have been reposted, return the maximum sum
            if x == 0:
                return max_sum
    # If not all pictures can be reposted, return -1
    if x > 0:
        return -1
    return max_sum

