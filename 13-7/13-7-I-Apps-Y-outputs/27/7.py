
def get_max_beauty(n, k, x, a):
    # Initialize variables
    beauty_sum = 0
    reposted_pictures = 0
    current_segment_length = 0
    max_segment_length = 0

    # Iterate through the array of picture beauties
    for i in range(n):
        # If the current picture is reposted, add its beauty to the total beauty sum
        if i < x:
            beauty_sum += a[i]
            reposted_pictures += 1

        # If the current picture is not reposted, check if it starts a new segment
        else:
            # If the current segment length is 0, start a new segment
            if current_segment_length == 0:
                current_segment_length = 1

            # If the current segment length is greater than 0, increment the segment length
            else:
                current_segment_length += 1

            # If the current segment length is greater than the maximum segment length, update the maximum segment length
            if current_segment_length > max_segment_length:
                max_segment_length = current_segment_length

            # If the current segment length is equal to the minimum segment length, break the loop
            if current_segment_length == k:
                break

    # If the total number of reposted pictures is not equal to the number of pictures Vova is ready to repost, return -1
    if reposted_pictures != x:
        return -1

    # Return the maximum sum of beauty values of reposted pictures
    return beauty_sum

